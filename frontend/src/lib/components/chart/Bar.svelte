<script lang="ts">
	import Chart, { type ChartOptions } from 'chart.js/auto';
	import { onMount } from 'svelte';

	export let title = 'Bar Chart';
	export let labels = [
		'Label 1',
		'Label 2',
		'Label 3',
		'Label 4',
		'Label 5',
		'Label 6',
		'Label 7',
		'Label 8',
		'Label 9',
		'Label 10'
	];
	export let data = [12, 19, 3, 5, 44, 12, 3, 1, 3, 66];
	let canvas: HTMLCanvasElement;

	onMount(() => {
		// Sample data
		let dataConfig = {
			labels,
			datasets: [
				{
					backgroundColor: '#b6c4cc', // Color for bars
					borderRadius: 10,
					// borderWidth: 2, // Border width for bars
					data // Actual data values
				}
			]
		};

		// Chart configuration
		const options: ChartOptions = {
			responsive: true,
			scales: {
				x: {
					grid: {
						display: false
					}
				},
				y: {
					grid: {
						display: false
					}
				}
			},
			plugins: {
				title: {
					display: true,
					text: title,
					color: '#1c1c1c',
					font: {
						size: 20,
						weight: 'bold',
						family: "'Arial', 'sans-serif'",
						lineHeight: '1.75rem'
					},
					align: 'start',
					padding: {
						top: 0,
						bottom: 20
					}
				}
			},
			maintainAspectRatio: false
		};

		// Create the bar chart
		new Chart(canvas, {
			type: 'bar', // Specify the chart type
			data: dataConfig,
			options
		});
	});
</script>

<canvas class="bg-primary-300" bind:this={canvas}></canvas>
