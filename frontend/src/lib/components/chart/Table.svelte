<script lang="ts">
	import { formatNumberToDollar } from '$components/utils';

	export let tableWidth: string;
	export let tableColumns: string[] = [];
	export let tableRows: (string | number)[][] = [];
	export let tableData:
		| {
				[key: string]: any;
		  }
		| undefined = undefined;

	export let rowToHighlight: string | null = null;

	// Example of tableData object:
	// AverageSalaryPerExperience: {
	// 					'0 to 1 years': null,
	// 					'2 to 4 years': {
	// 						yearly: 48093.0,
	// 						hourly: 33.31
	// 					},
	// 					'5 to 9 years': {
	// 						yearly: 56744.96,
	// 						hourly: 39.31
	// 					},
	// 					'10 or more years': {
	// 						yearly: 65562.41,
	// 						hourly: 45.42
	// 					},
	// 				}
	if (tableData) {
		tableRows = Object.entries(tableData).map(([key, value]) => {
			if (typeof value === 'object' && value !== null) {
				return [key, formatNumberToDollar(value.yearly), formatNumberToDollar(value.hourly)];
			}
			if (value === null) {
				return [key, 'Not Enough Data', 'Not Enough Data'];
			}
			return [];
		});

		tableRows = tableRows.filter((row) => row.length > 0);
	}
</script>

<table class="{tableWidth} min-h-48 xl:min-h-96">
	<thead>
		<tr class="text-sm font-semibold tracking-wide text-left text-leftuppercase bg-secondary-400">
			{#each tableColumns as column}
				<th class="p-2 border border-gray-300 xl:px-4 xl:py-3">{column}</th>
			{/each}
		</tr>
	</thead>
	<tbody class="bg-white">
		{#each tableRows as row}
			<tr class={row[0] === rowToHighlight ? 'bg-indigo-100' : ''}>
				{#each row as field}
					<td class="px-2 py-1 font-medium border border-gray-300 xl:px-4 text-ms">{field}</td>
				{/each}
			</tr>
		{/each}
	</tbody>
</table>
