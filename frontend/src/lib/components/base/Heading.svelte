<script lang="ts">
	export let headingType: 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6' = 'h1';
	export let customClass = '';
</script>

{#if headingType === 'h1'}
	<h1 class="{customClass} text-4xl font-bold">
		<slot />
	</h1>
{:else if headingType === 'h2'}
	<h2 class="{customClass} text-3xl font-bold">
		<slot />
	</h2>
{:else if headingType === 'h3'}
	<h3 class="{customClass} text-2xl font-bold">
		<slot />
	</h3>
{:else if headingType === 'h4'}
	<h4 class="{customClass} text-xl font-bold">
		<slot />
	</h4>
{:else if headingType === 'h5'}
	<h5 class="{customClass} text-lg font-bold">
		<slot />
	</h5>
{:else if headingType === 'h6'}
	<h6 class="{customClass} text-base font-bold">
		<slot />
	</h6>
{/if}
