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
		user: {
			[key: string]: string;
		};
	}

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

	let salaryDataPromise: Promise<OverviewAndDashboardData> | undefined;

	let isFetchingSalaryData = false;
	function ToggleDisableEvaluateButton() {
		// It returns nothing because I want to execute the function inside the {}
		isFetchingSalaryData = !isFetchingSalaryData;
		return '';
	}

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

<main class="w-full mb-24">
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
				class="flex items-center justify-center px-3 py-3 {isFetchingSalaryData
					? 'bg-gray-200'
					: 'bg-blue-200 hover:bg-blue-100'} rounded max-h-10"
				type="submit"
				disabled={isFetchingSalaryData}
			>
				Evaluate
			</button>
		</form>
	</section>
	{#if salaryDataPromise}
		{#await salaryDataPromise}
			<p>...computing</p>
			{ToggleDisableEvaluateButton()}
		{:then overviewAndDashboardData}
			{ToggleDisableEvaluateButton()}
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
						title="Predicted Hourly rate for 40-hour week (CAD)"
						value={formatNumberToDollar(overviewAndDashboardData.overview.userSalary.hourly)}
					/>

					<OverviewCard
						color="bg-primary-400"
						width="col-span-3"
						title="Average Yearly Rate: {overviewAndDashboardData.user
							.City}, {overviewAndDashboardData.user.Experience} Exp. (CAD)"
						value={overviewAndDashboardData.overview.averageSalaryForCity.yearly
							? formatNumberToDollar(overviewAndDashboardData.overview.averageSalaryForCity.yearly)
							: 'Not Enough Data'}
					/>

					<OverviewCard
						color="bg-secondary-400"
						width="col-span-3"
						title="Average Hourly Rate:{overviewAndDashboardData.user
							.City}, {overviewAndDashboardData.user.Experience} Exp. (CAD)"
						value={overviewAndDashboardData.overview.averageSalaryForCity.hourly
							? formatNumberToDollar(overviewAndDashboardData.overview.averageSalaryForCity.hourly)
							: 'Not Enough Data'}
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
							>{`Average ${overviewAndDashboardData.user.Title} Salary in ${overviewAndDashboardData.user.City} by Experience`}</Heading
						>
						<Table
							tableWidth="w-full"
							tableColumns={['Experience', 'Yearly Salary (CAD)', 'Hourly Salary (CAD)']}
							tableData={overviewAndDashboardData.dashboard.AverageSalaryPerExperience}
							rowToHighlight={overviewAndDashboardData.user.Experience}
						/>
					</div>

					<div
						class="order-2 p-2 col-span-full 2xl:col-span-6 min-h-96 xl:p-6 bg-secondary-300 rounded-xl"
					>
						<Bar
							title={`Average ${overviewAndDashboardData.user.Title} Salary (CAD) in Canadian Cities`}
							objData={overviewAndDashboardData.dashboard.AverageSalaryPerCity}
							barToHighlight={overviewAndDashboardData.user.City}
						/>
					</div>
					<div
						class="flex flex-col order-3 gap-4 p-2 col-span-full 2xl:col-span-4 2xl:order-4 bg-secondary-300 rounded-xl xl:p-6"
					>
						<Heading headingType="h4"
							>{`Average Salary in ${overviewAndDashboardData.user.City} by Industry`}</Heading
						>
						<Table
							tableWidth="col-span-4"
							tableColumns={['Industry', 'Yearly Salary (CAD)', 'Hourly Salary (CAD)']}
							tableData={overviewAndDashboardData.dashboard.AverageSalaryPerIndustry}
							rowToHighlight={overviewAndDashboardData.user.Industry}
						/>
					</div>

					<div
						class="order-4 p-2 col-span-full 2xl:col-span-6 2xl:order-3 min-h-96 xl:p-6 bg-secondary-300 rounded-xl"
					>
						<Bar
							title={`Average Salary (CAD) per Title in ${overviewAndDashboardData.user.City}`}
							objData={overviewAndDashboardData.dashboard.AverageSalaryPerTitle}
							barToHighlight={overviewAndDashboardData.user.Title}
						/>
					</div>
				</div>
			</section>
		{:catch error}
			{ToggleDisableEvaluateButton()}

			<p style="color: red">Error!!! Retry please.</p>
		{/await}
	{:else}
		<Heading headingType="h2">No data to display</Heading>
		<p class="mt-5 text-base font-medium">Please use the fields above to evaluate your salary.</p>
	{/if}
</main>
