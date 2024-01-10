<script lang="ts">
	import { page } from '$app/stores';
	import logo from '../../../assets/logo.png';
	import menuClose from '../../../assets/menu-close.png';
	import menuOpen from '../../../assets/menu-open.png';

	$: routeId = $page.route.id;
	let isNavToggled = false;

	function toggleNavMenu() {
		isNavToggled = !isNavToggled;
	}

	const navs = [
		{
			name: 'Home',
			link: '/'
		},
		{
			name: 'Data',
			link: '/data'
		}
	];
</script>

<aside
	class="fixed z-20 flex flex-col w-full gap-5 px-3 mt-12 bg-white border-r lg:px-0 lg:flex-col lg:w-64 lg:h-full lg:mt-0 border-r-gray-300"
>
	<div class="flex flex-row items-center justify-between w-full h-16 lg:h-auto">
		<img
			src={logo}
			alt="Logo of the company"
			class="self-start object-contain h-full lg:w-auto lg:h-auto"
		/>
		<button on:click={toggleNavMenu}>
			<img
				src={isNavToggled ? menuClose : menuOpen}
				alt="open navigation bar button"
				class="block lg:hidden"
			/>
		</button>
	</div>
	<ul
		class="{isNavToggled
			? 'flex'
			: 'hidden'} lg:flex flex-col w-full h-full gap-4 lg:px-2 text-left bg-white"
	>
		{#each navs as { link, name }}
			<li
				class="{link === routeId
					? 'bg-gray-200'
					: ''} w-full px-1 py-2 text-2xl rounded lg:px-2 hover:underline"
			>
				<a href={link} title={name}>{name}</a>
			</li>
		{/each}
		<li class="px-1 py-2 text-2xl lg:px-2 hover:underline">
			<a
				href="https://github.com/MounirAia/Canadian-Tech-Salary-Prediction-App"
				target="_blank"
				title="Github Repo"
			>
				Github Repo
			</a>
		</li>
	</ul>
</aside>
