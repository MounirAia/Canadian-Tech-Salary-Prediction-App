<script lang="ts">
	import Heading from '$components/base/Heading.svelte';
	import Bar from '$components/chart/Bar.svelte';
	import Table from '$components/chart/Table.svelte';
	import { PUBLIC_BACKEND_DOMAIN } from '$env/static/public';
	import { onMount } from 'svelte';

	let selectStatements: Map<string, { options: { output: string; value: string | number }[] }> =
		new Map();

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
				}
				selectStatements = new Map([...selectStatements]);
			});
	});
</script>

<div class="grid grid-cols-1 grid-rows-1 gap-y-10 w-full mt-16 ml-64">
	<main class="col-span-1 ml-8 mr-72 mb-24">
		<section class="fields w-full mb-24">
			<Heading headingType="h2" customClass="mb-5">Evaluate</Heading>
			<div class="grid grid-cols-10 gap-x-8 gap-y-10">
				{#each [...selectStatements] as [title, { options }]}
					<select
						class="col-span-1 py-3 px-4 border border-gray-300 text-sm rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
					>
						<option disabled selected value="">{title}</option>
						{#each options as option}
							<option value={option.value}>{option.output}</option>
						{/each}
					</select>
				{/each}

				<button
					class="col-start-8 col-span-3 px-3 py-3 bg-blue-200 hover:bg-blue-100 rounded max-h-10 flex items-center justify-center"
				>
					Evaluate
				</button>

				<div class="col-span-2 min-h-28 p-6 flex flex-col gap-5 bg-[#E3F5FF] rounded-2xl">
					<p class="text-base font-medium">Yearly base salary in CAD</p>
					<Heading headingType="h3" customClass="tracking-wider">112 000 $</Heading>
				</div>
				<div class="col-span-2 min-h-28 p-6 flex flex-col gap-5 bg-[#E5ECF6] rounded-2xl">
					<p class="text-base font-medium">Hourly rate for 40-hour week</p>
					<Heading headingType="h3" customClass="tracking-wider">32$</Heading>
				</div>
				<div class="col-span-3 min-h-28 p-6 flex flex-row text-white bg-accent-300 rounded-2xl">
					<div class="flex flex-col gap-5 min-w-[80%]">
						<Heading headingType="h3" customClass="tracking-wider">Your Support Counts</Heading>
						<p class="text-base font-medium">
							You can enhance the machine learning model quality by helping us!
						</p>
					</div>
					<a
						href="/"
						class="bg-white hover:bg-slate-200 transition text-black text-base self-end rounded px-3 py-1 w-full flex flex-row justify-between items-center"
					>
						<p>Help Us</p>
						<span class="material-symbols-outlined"> east </span>
					</a>
				</div>
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
						tableRows={[
							['Yes', '22', 'Acceptable'],
							['Yes', '22', 'Acceptable'],
							['Yes', '22', 'Acceptable'],
							['Yes', '22', 'Acceptable']
						]}
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
					<Heading headingType="h4">Expected Salary Based on Experience</Heading>

					<Table
						tableWidth="col-span-4"
						tableColumns={['Experience', 'Yearly Salary (CAD)', 'Hourly Salary (CAD)']}
						tableRows={[
							['Yes', '22', 'Acceptable'],
							['Yes', '22', 'Acceptable'],
							['Yes', '22', 'Acceptable'],
							['Yes', '22', 'Acceptable']
						]}
					/>
				</div>
			</div>
		</section>
	</main>
</div>
