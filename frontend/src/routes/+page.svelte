<script lang="ts">
	import Heading from '$components/base/Heading.svelte';
	import OverviewCard from '$components/base/OverviewCard.svelte';
	import Bar from '$components/chart/Bar.svelte';
	import Table from '$components/chart/Table.svelte';
	import { formatNumberToDollar } from '$components/utils';
	import { PUBLIC_BACKEND_DOMAIN } from '$env/static/public';
	import { onMount } from 'svelte';

	let selectStatements: Map<string, { options: { output: string; value: string | number }[] }> =
		new Map();

	// Select input values to send to backend
	let selectedValues: { [key: string]: string } = {};

	interface OverviewAndDashboardData {
		overview: {
			userSalary: {
				yearly: number;
				hourly: number;
			};
			averageSalaryForCity: {
				yearly: number;
				hourly: number;
				userCity: string;
				userExperience: string;
			};
		};
		dashboard: {
			AverageSalaryPerExperience: {
				[key: string]:
					| {
							yearly: number;
							hourly: number;
					  }
					| string
					| null;
				user: string;
			};
			AverageSalaryPerCity: {
				[key: string]: string | number | null;
				user: string;
			};
			AverageSalaryPerTitle: {
				[key: string]: string | number | null;
				user: string;
			};
			AverageSalaryPerIndustry: {
				[key: string]:
					| {
							yearly: number;
							hourly: number;
					  }
					| string
					| null;
				user: string;
			};
		};
	}

	// TODO: Set to undefined after testing
	let overviewAndDashboardData: OverviewAndDashboardData = {
		overview: {
			userSalary: {
				yearly: 69340.0,
				hourly: 48.03
			},
			averageSalaryForCity: {
				yearly: 76431.71,
				hourly: 52.94,
				userCity: 'Montréal Region',
				userExperience: '5 to 9 years'
			}
		},
		dashboard: {
			AverageSalaryPerExperience: {
				'0 to 1 years': null,
				'2 to 4 years': {
					yearly: 48093.0,
					hourly: 33.31
				},
				'5 to 9 years': {
					yearly: 56744.96,
					hourly: 39.31
				},
				'10 or more years': {
					yearly: 65562.41,
					hourly: 45.42
				},
				user: '5 to 9 years'
			},
			AverageSalaryPerCity: {
				'Edmonton Region': 142008.06,
				'Lower Mainland–Southwest Region': 86969.7,
				'Hamilton–Niagara Peninsula Region': 83632.79,
				'Ottawa Region': 78985.48,
				'Thompson–Okanagan Region': 75716.4,
				'Kingston–Pembroke Region': 63249.92,
				'Halifax Region': 63188.46,
				'Vancouver Island and Coast Region': 62927.33,
				'Winnipeg Region': 61371.74,
				'Annapolis Valley Region': 60231.0,
				'Montréal Region': 59627.41,
				user: 'Montréal Region'
			},
			AverageSalaryPerTitle: {
				'Engineering manager': 134997.91,
				'Senior Executive (C-Suite, VP, etc.)': 134989.67,
				'Product manager': 134610.33,
				'Developer, embedded applications or devices': 122752.92,
				'Engineer, site reliability': 92270.0,
				'Developer, game or graphics': 88573.0,
				'Database administrator': 85378.0,
				'Developer, QA or test': 85111.5,
				'DevOps specialist': 83101.25,
				'Hardware Engineer': 80547.67,
				'Developer, back-end': 59627.41,
				user: 'Developer, back-end'
			},
			AverageSalaryPerIndustry: {
				Insurance: {
					yearly: 96950.5,
					hourly: 67.16
				},
				'Retail and Consumer Services': {
					yearly: 83380.72,
					hourly: 57.76
				},
				'Higher Education': {
					yearly: 82646.0,
					hourly: 57.25
				},
				Healthcare: {
					yearly: 60216.22,
					hourly: 41.71
				},
				user: 'Healthcare'
			}
		}
	};

	onMount(() => {
		fetch(`${PUBLIC_BACKEND_DOMAIN}/api/index`)
			.then((res) => res.json())
			.then((data) => {
				for (const key in data) {
					const options = [];

					for (const value of data[key]) {
						options.push({ output: value, value });
					}
					selectStatements.set(key, { options });

					selectedValues[key] = '';
				}
				selectStatements = new Map([...selectStatements]);
			});
	});

	let salaryDataPromise: Promise<any> | undefined;

	async function getSalaryData() {
		const res = await fetch(`${PUBLIC_BACKEND_DOMAIN}/api/salary`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(selectedValues)
		});
		const data = await res.json();
		return data;
	}

	async function onSubmit() {
		salaryDataPromise = getSalaryData();
	}
</script>

<main class="w-full px-4 mb-24 xl:px-8">
	<section class="w-full mb-24 fields">
		<Heading headingType="h2" customClass="mb-5">Evaluate</Heading>
		<form class="grid mb-24 form-grid gap-x-8 gap-y-4" on:submit|preventDefault={onSubmit}>
			{#each [...selectStatements] as [title, { options }]}
				<select
					bind:value={selectedValues[title]}
					class="w-full px-4 py-3 text-sm leading-tight border border-gray-400 rounded focus:outline-none focus:bg-white focus:border-gray-500"
					required
					disabled={title === 'Country'}
				>
					<option disabled selected value="">{title === 'Country' ? 'Canada' : title}</option>
					{#each options as option}
						<option value={option.value}>{option.output}</option>
					{/each}
				</select>
			{/each}

			<button
				class="flex items-center justify-center px-3 py-3 bg-blue-200 rounded hover:bg-blue-100 max-h-10"
				type="submit"
			>
				Evaluate
			</button>
		</form>
	</section>
	<section class="mb-24 overview">
		<Heading headingType="h2" customClass="mb-5">Overview</Heading>
		<div class="grid sm:grid-cols-3 lg:grid-cols-6 2xl:grid-cols-12 gap-y-5 gap-x-8">
			<OverviewCard
				color="bg-primary-400"
				width="col-span-3"
				title="Predicted Yearly base salary (CAD)"
				value={formatNumberToDollar(overviewAndDashboardData.overview.userSalary.yearly)}
			/>

			<OverviewCard
				color="bg-secondary-400"
				width="col-span-3"
				title="Predicted Hourly rate for 40-hour week"
				value={formatNumberToDollar(overviewAndDashboardData.overview.userSalary.hourly)}
			/>

			<OverviewCard
				color="bg-primary-400"
				width="col-span-3"
				title="Average Yearly Rate: {overviewAndDashboardData.overview.averageSalaryForCity
					.userCity}, {overviewAndDashboardData.overview.averageSalaryForCity
					.userExperience} Exp. (CAD)"
				value={formatNumberToDollar(overviewAndDashboardData.overview.averageSalaryForCity.yearly)}
			/>

			<OverviewCard
				color="bg-secondary-400"
				width="col-span-3"
				title="Average Hourly Rate: {overviewAndDashboardData.overview.averageSalaryForCity
					.userCity}, {overviewAndDashboardData.overview.averageSalaryForCity
					.userExperience} Exp. (CAD)"
				value={formatNumberToDollar(overviewAndDashboardData.overview.averageSalaryForCity.hourly)}
			/>
		</div>
	</section>
	<section class="w-full dashboard">
		<Heading headingType="h2" customClass="mb-5">Dashboard</Heading>
		<p class="mb-5 text-base font-medium">
			This dashboard serves as a visual representation of the data used to build the machine
			learning model.
		</p>
		<div class="grid grid-cols-10 gap-8">
			<div
				class="flex flex-col order-1 gap-4 p-2 col-span-full 2xl:col-span-4 bg-secondary-300 rounded-xl xl:p-6"
			>
				<Heading headingType="h4"
					>{`Average ${selectedValues['Title']} Salary in ${selectedValues['City']} by Experience`}</Heading
				>
				<Table
					tableWidth="w-full"
					tableColumns={['Experience', 'Yearly Salary (CAD)', 'Hourly Salary (CAD)']}
					tableData={overviewAndDashboardData.dashboard.AverageSalaryPerExperience}
					rowToHighlight={overviewAndDashboardData.dashboard.AverageSalaryPerExperience.user}
				/>
			</div>

			<div
				class="order-2 p-2 col-span-full 2xl:col-span-6 min-h-96 xl:p-6 bg-secondary-300 rounded-xl"
			>
				<Bar
					title={`Average ${selectedValues['Title']} Salary (CAD) in Canadian Cities`}
					objData={overviewAndDashboardData.dashboard.AverageSalaryPerCity}
					barToHighlight={overviewAndDashboardData.dashboard.AverageSalaryPerCity?.user}
				/>
			</div>
			<div
				class="flex flex-col order-3 gap-4 p-2 col-span-full 2xl:col-span-4 xl:order-4 bg-secondary-300 rounded-xl xl:p-6"
			>
				<Heading headingType="h4"
					>{`Average Salary in ${selectedValues['City']} by Industry`}</Heading
				>
				<Table
					tableWidth="col-span-4"
					tableColumns={['Industry', 'Yearly Salary (CAD)', 'Hourly Salary (CAD)']}
					tableData={overviewAndDashboardData.dashboard.AverageSalaryPerIndustry}
					rowToHighlight={overviewAndDashboardData.dashboard.AverageSalaryPerIndustry.user}
				/>
			</div>

			<div
				class="order-4 p-2 col-span-full 2xl:col-span-6 xl:order-3 min-h-96 xl:p-6 bg-secondary-300 rounded-xl"
			>
				<Bar
					title={`Average Salary (CAD) per Title in ${selectedValues['City']}`}
					objData={overviewAndDashboardData.dashboard.AverageSalaryPerTitle}
					barToHighlight={overviewAndDashboardData.dashboard.AverageSalaryPerTitle?.user}
				/>
			</div>
		</div>
	</section>
	{#if salaryDataPromise}
		{#await salaryDataPromise}
			<p>...computing</p>
		{:then overviewAndDashboardData}
			<section class="mb-24 overview">
				<Heading headingType="h2" customClass="mb-5">Overview</Heading>
				<div class="grid grid-cols-12 gap-x-8">
					<OverviewCard
						color="bg-primary-400"
						width="col-span-3"
						title="Predicted Yearly base salary (CAD)"
						value={formatNumberToDollar(overviewAndDashboardData.overview.userSalary.yearly)}
					/>

					<OverviewCard
						color="bg-secondary-400"
						width="col-span-3"
						title="Predicted Hourly rate for 40-hour week"
						value={formatNumberToDollar(overviewAndDashboardData.overview.userSalary.hourly)}
					/>

					<OverviewCard
						color="bg-primary-400"
						width="col-span-3"
						title="Average Yearly Rate: {overviewAndDashboardData.overview.averageSalaryForCity
							.userCity}, {overviewAndDashboardData.overview.averageSalaryForCity
							.userExperience} Exp. (CAD)"
						value={formatNumberToDollar(
							overviewAndDashboardData.overview.averageSalaryForCity.yearly
						)}
					/>

					<OverviewCard
						color="bg-secondary-400"
						width="col-span-3"
						title="Average Hourly Rate: {overviewAndDashboardData.overview.averageSalaryForCity
							.userCity}, {overviewAndDashboardData.overview.averageSalaryForCity
							.userExperience} Exp. (CAD)"
						value={formatNumberToDollar(
							overviewAndDashboardData.overview.averageSalaryForCity.hourly
						)}
					/>
				</div>
			</section>
			<section class="w-full dashboard">
				<Heading headingType="h2" customClass="mb-5">Dashboard</Heading>
				<p class="mb-5 text-base font-medium">
					This dashboard serves as a visual representation of the data used to build the machine
					learning model.
				</p>
				<div class="grid grid-cols-10 gap-8">
					<div
						class="flex flex-col gap-4 p-6 col-span-full 2xl:col-span-4 bg-secondary-300 rounded-xl"
					>
						<Heading headingType="h4"
							>{`Average ${selectedValues['Title']} Salary in ${selectedValues['City']} by Experience`}</Heading
						>
						<Table
							tableWidth="w-full"
							tableColumns={['Experience', 'Yearly Salary (CAD)', 'Hourly Salary (CAD)']}
							tableData={overviewAndDashboardData.dashboard.AverageSalaryPerExperience}
							rowToHighlight={overviewAndDashboardData.dashboard.AverageSalaryPerExperience.user}
						/>
					</div>

					<div class="p-6 col-span-full 2xl:col-span-6 bg-secondary-300 rounded-xl">
						<Bar
							title={`Average ${selectedValues['Title']} Salary in Canadian Cities`}
							objData={overviewAndDashboardData.dashboard.AverageSalaryPerCity}
							barToHighlight={overviewAndDashboardData.dashboard.AverageSalaryPerCity?.user}
						/>
					</div>
					<div class="p-6 col-span-full 2xl:col-span-6 bg-secondary-300 rounded-xl">
						<Bar
							title={`Average Salary per Title in ${selectedValues['City']}`}
							objData={overviewAndDashboardData.dashboard.AverageSalaryPerTitle}
							barToHighlight={overviewAndDashboardData.dashboard.AverageSalaryPerTitle?.user}
						/>
					</div>
					<div
						class="flex flex-col gap-4 p-6 col-span-full 2xl:col-span-4 bg-secondary-300 rounded-xl"
					>
						<Heading headingType="h4"
							>{`Average Salary in ${selectedValues['City']} by Industry`}</Heading
						>
						<Table
							tableWidth="col-span-4"
							tableColumns={['Industry', 'Yearly Salary (CAD)', 'Hourly Salary (CAD)']}
							tableData={overviewAndDashboardData.dashboard.AverageSalaryPerIndustry}
							rowToHighlight={overviewAndDashboardData.dashboard.AverageSalaryPerIndustry.user}
						/>
					</div>
				</div>
			</section>
		{:catch error}
			<p style="color: red">Error!!!</p>
		{/await}
	{:else}
		<Heading headingType="h2">No data to display</Heading>
		<p class="mt-5 text-base font-medium">Please use the fields above to evaluate your salary.</p>
	{/if}
</main>
