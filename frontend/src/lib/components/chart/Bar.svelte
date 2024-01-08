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

	export let objData: { [key: string]: any } | undefined;

	export let barToHighlight: string | null = null;

	let backgroundColor: string | string[] = '#b6c4cc';

	if (objData) {
		data = Object.values(objData);
		labels = Object.keys(objData);
		const unecessaryIndex = labels.indexOf('user');
		if (unecessaryIndex > -1) {
			labels.splice(unecessaryIndex, 1);
			data.splice(unecessaryIndex, 1);
		}

		if (barToHighlight) {
			backgroundColor = [];
			for (let i = 0; i < labels.length; i++) {
				if (labels[i] === barToHighlight) {
					backgroundColor[i] = '#818cf8';
					continue;
				}
				backgroundColor[i] = '#b6c4cc';
			}
		}
	}

	let canvas: HTMLCanvasElement;

	onMount(() => {
		// Sample data
		let dataConfig = {
			labels,
			datasets: [
				{
					backgroundColor: backgroundColor, // Color for bars
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
						bottom: 30
					}
				},
				legend: {
					display: false
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
