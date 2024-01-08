<script lang="ts">
	import Heading from './Heading.svelte';

	export let title: string;
	export let value: string;
	export let width: string;
	export let color: 'bg-[#E5ECF6]' | 'bg-[#E3F5FF]' = 'bg-[#E5ECF6]';
</script>

<div class="{width} {color} min-h-28 px-6 py-8 flex flex-col gap-5 bg-[#E5ECF6] rounded-2xl">
	<p class="text-base font-medium">
		{title}
	</p>
	<Heading headingType="h3" customClass="tracking-wider">{value}</Heading>
</div>
