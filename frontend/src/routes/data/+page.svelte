<script lang="ts">
	import Heading from '$components/base/Heading.svelte';
	import OverviewCard from '$components/base/OverviewCard.svelte';
	import Bar from '$components/chart/Bar.svelte';
	import { PUBLIC_BACKEND_DOMAIN } from '$env/static/public';
	import { onMount } from 'svelte';

	async function getCanadaData() {
		const res = await fetch(`${PUBLIC_BACKEND_DOMAIN}/api/canada`);
		const data = await res.json();
		return data;
	}

	let canadaDataPromise: Promise<any> | undefined;

	onMount(async () => {
		canadaDataPromise = getCanadaData();
	});
</script>

{#if canadaDataPromise}
	{#await canadaDataPromise}
		<p>...loading the data a moment</p>
	{:then canadaData}
		<section class="mb-24 overview">
			<Heading headingType="h2" customClass="mb-5">Overview</Heading>
			<div class="grid sm:grid-cols-3 lg:grid-cols-6 2xl:grid-cols-12 gap-y-5 gap-x-8">
				<OverviewCard
					color="bg-primary-400"
					width="col-span-3"
					title="Number of Files Processed"
					value={canadaData.numberFileProcessed}
				/>

				<OverviewCard
					color="bg-secondary-400"
					width="col-span-3"
					title="Number of Rows in Canada Database"
					value={canadaData.numberRows}
				/>

				<OverviewCard
					color="bg-primary-400"
					width="col-span-3"
					title="Number of Cities Covered"
					value={canadaData.numberCities}
				/>

				<OverviewCard
					color="bg-secondary-400"
					width="col-span-3"
					title="Number of Titles Covered"
					value={canadaData.numberTitles}
				/>
			</div>
		</section>
		<section class="w-full mb-24 dashboard">
			<Heading headingType="h2" customClass="mb-5">Dashboard</Heading>
			<p class="mb-5 text-base font-medium">
				There is more information on how I constructed the Canadian dataset in my read me file on my <a
					class="text-blue-500 hover:underline"
					href="https://github.com/MounirAia/Canadian-Tech-Salary-Prediction-App?tab=readme-ov-file#data-processing-pipeline"
					target="_blank">GitHub</a
				>.
			</p>
			<div class="grid grid-cols-10 gap-8">
				<div class="order-2 p-2 bg-secondary-300 col-span-full min-h-96 xl:p-6 rounded-xl">
					<Bar
						title={`Proportion of Data by Salary Range`}
						objData={canadaData.salaryRangeDistribution}
					/>
				</div>
				<div
					class="order-2 p-2 col-span-full 2xl:col-span-5 min-h-96 xl:p-6 bg-secondary-300 rounded-xl"
				>
					<Bar
						title={`Proportion of Data by City`}
						objData={canadaData.cityProportionDistribution}
					/>
				</div>
				<div
					class="order-2 p-2 col-span-full 2xl:col-span-5 min-h-96 xl:p-6 bg-secondary-300 rounded-xl"
				>
					<Bar
						title={`Proportion of Data by Experience`}
						objData={canadaData.experienceProportionDistribution}
					/>
				</div>
				<div
					class="order-2 p-2 col-span-full 2xl:col-span-5 min-h-96 xl:p-6 bg-secondary-300 rounded-xl"
				>
					<Bar
						title={`Proportion of Data by Company Size`}
						objData={canadaData.companySizeProportionDistribution}
					/>
				</div>
				<div
					class="order-2 p-2 col-span-full 2xl:col-span-5 min-h-96 xl:p-6 bg-secondary-300 rounded-xl"
				>
					<Bar
						title={`Proportion of Data by Industry`}
						objData={canadaData.industryProportionDistribution}
					/>
				</div>
				<div class="order-2 p-2 col-span-full min-h-96 xl:p-6 bg-secondary-300 rounded-xl">
					<Bar
						title={`Proportion of Data by Title`}
						objData={canadaData.titleProportionDistribution}
					/>
				</div>
			</div>
		</section>
	{:catch error}
		<p style="color: red">Error!!! Reload the page.</p>
	{/await}
{/if}
