<script lang="ts">
	export let tableWidth: string;
	export let tableColumns: string[] = [];
	export let tableRows: string[][] = [];
</script>

<table class="{tableWidth} min-h-96">
	<thead>
		<tr class="text-left text-sm font-semibold tracking-wide text-leftuppercase bg-secondary-400">
			{#each tableColumns as column}
				<th class="px-4 py-3 border border-gray-300">{column}</th>
			{/each}
		</tr>
	</thead>
	<tbody class="bg-white">
		{#each tableRows as row}
			<tr class="">
				{#each row as field}
					<td class="px-4 text-ms font-medium border border-gray-300">{field}</td>
				{/each}
			</tr>
		{/each}
	</tbody>
</table>
