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

	// Set to undefined after testing
	let overviewAndDashboardData: undefined | OverviewAndDashboardData = {
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
				'Montréal Region': 59627.41,
				user: 'Montréal Region',
				'Edmonton Region': 142008.06,
				'Lower Mainland–Southwest Region': 86969.7,
				'Hamilton–Niagara Peninsula Region': 83632.79,
				'Ottawa Region': 78985.48,
				'Thompson–Okanagan Region': 75716.4,
				'Kingston–Pembroke Region': 63249.92,
				'Halifax Region': 63188.46,
				'Vancouver Island and Coast Region': 62927.33,
				'Winnipeg Region': 61371.74
			},
			AverageSalaryPerTitle: {
				'Developer, back-end': 59627.41,
				user: 'Developer, back-end',
				'Engineering manager': 134997.91,
				'Senior Executive (C-Suite, VP, etc.)': 134989.67,
				'Product manager': 134610.33,
				'Developer, embedded applications or devices': 122752.92,
				'Engineer, site reliability': 92270.0,
				'Developer, game or graphics': 88573.0,
				'Database administrator': 85378.0,
				'Developer, QA or test': 85111.5,
				'DevOps specialist': 83101.25
			},
			AverageSalaryPerIndustry: {
				Healthcare: {
					yearly: 60216.22,
					hourly: 41.71
				},
				user: 'Healthcare',
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
				}
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

	function onSubmit() {
		fetch(`${PUBLIC_BACKEND_DOMAIN}/api/salary`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(selectedValues)
		})
			.then((res) => res.json())
			.then((data) => {
				overviewAndDashboardData = data;
				console.log(overviewAndDashboardData);
			});
	}
</script>

<div class="grid grid-cols-1 grid-rows-1 gap-y-10 w-full mt-16 ml-64">
	<main class="col-span-1 ml-8 mr-72 mb-24">
		<section class="fields w-full mb-24">
			<Heading headingType="h2" customClass="mb-5">Evaluate</Heading>
			<form class="grid grid-cols-12 gap-x-8 mb-24" on:submit|preventDefault={onSubmit}>
				<div class="col-span-10 flex flex-row gap-4 justify-between">
					{#each [...selectStatements] as [title, { options }]}
						<select
							bind:value={selectedValues[title]}
							class="w-full py-3 px-4 border border-gray-400 text-sm rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
						>
							<option disabled selected value="">{title}</option>
							{#each options as option}
								<option value={option.value}>{option.output}</option>
							{/each}
						</select>
					{/each}
				</div>

				<button
					class="col-span-2 px-3 py-3 bg-blue-200 hover:bg-blue-100 rounded max-h-10 flex items-center justify-center"
					type="submit"
				>
					Evaluate
				</button>
			</form>
		</section>
		{#if overviewAndDashboardData}
			<section class="overview mb-24">
				<Heading headingType="h2" customClass="mb-5">Overview</Heading>
				<div class="grid grid-cols-12 gap-x-8">
					<OverviewCard
						color="bg-[#E3F5FF]"
						width="col-span-3"
						title="Predicted Yearly base salary (CAD)"
						value={formatNumberToDollar(overviewAndDashboardData.overview.userSalary.yearly)}
					/>

					<OverviewCard
						color="bg-[#E5ECF6]"
						width="col-span-3"
						title="Predicted Hourly rate for 40-hour week"
						value={formatNumberToDollar(overviewAndDashboardData.overview.userSalary.hourly)}
					/>

					<OverviewCard
						color="bg-[#E3F5FF]"
						width="col-span-3"
						title="Average Yearly Rate: {overviewAndDashboardData.overview.averageSalaryForCity
							.userCity}, {overviewAndDashboardData.overview.averageSalaryForCity
							.userExperience} Exp. (CAD)"
						value={formatNumberToDollar(
							overviewAndDashboardData.overview.averageSalaryForCity.yearly
						)}
					/>

					<OverviewCard
						color="bg-[#E5ECF6]"
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
			<section class="dashboard w-full">
				<Heading headingType="h2" customClass="mb-5">Dashboard</Heading>
				<div class="grid grid-cols-10 gap-8">
					<div class="col-span-4 flex flex-col gap-4 bg-secondary-300 rounded-xl p-6">
						<Heading headingType="h4">Expected Salary Based on Experience</Heading>
						<Table
							tableWidth="w-full"
							tableColumns={['Experience', 'Yearly Salary (CAD)', 'Hourly Salary (CAD)']}
							tableData={overviewAndDashboardData.dashboard.AverageSalaryPerExperience}
							rowToHighlight={overviewAndDashboardData.dashboard.AverageSalaryPerExperience.user}
						/>
					</div>

					<div class="col-span-6 p-6 bg-secondary-300 rounded-xl">
						<Bar title="Average Salaries in 10 Canadian Cities" />
					</div>
					<div class="col-span-6 p-6 bg-secondary-300 rounded-xl">
						<Bar
							title="Average Salary per Role in the City"
							labels={['a', 'b', 'c']}
							data={[1, 2, 3]}
						/>
					</div>
					<div class="col-span-4 flex flex-col gap-4 bg-secondary-300 rounded-xl p-6">
						<Heading headingType="h4">Expected Salary Based on Industry</Heading>
						<Table
							tableWidth="col-span-4"
							tableColumns={['Industry', 'Yearly Salary (CAD)', 'Hourly Salary (CAD)']}
							tableData={overviewAndDashboardData.dashboard.AverageSalaryPerIndustry}
							rowToHighlight={overviewAndDashboardData.dashboard.AverageSalaryPerIndustry.user}
						/>
					</div>
				</div>
			</section>
		{:else}
			<Heading headingType="h2">No data to display</Heading>
			<p class="text-base font-medium mt-5">Please use the field above to evaluate your salary.</p>
		{/if}
	</main>
</div>
