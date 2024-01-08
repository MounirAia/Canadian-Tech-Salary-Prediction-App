<script>
	import Heading from '$components/base/Heading.svelte';
	import '../app.css';
	import logo from '../assets/logo.png';
</script>

<header
	class="w-full h-12 fixed top-0 ml-64 flex flex-row justify-start items-center gap-4 capitalize border-b pl-8 bg-white"
>
	<Heading headingType="h1" customClass="">Free Palestine</Heading>
	<div class="flex flex-col h-full flex-1">
		<div class="black w-full h-[33%] bg-black"></div>
		<div class="red-white w-full h-[33%]">
			<div class="red w-[30%] h-full bg-[#E4312b]"></div>
			<div class="white w-[70%] h-full bg-white"></div>
		</div>
		<div class="green w-full h-[35%] bg-[#149954]"></div>
	</div>
</header>

<aside class="fixed w-64 h-full flex flex-col gap-5 items-center border-r border-r-gray-300">
	<img src={logo} alt="Logo of the company" class="object-contain" />
	<ul class="flex flex-col text-left px-2 gap-4 w-full">
		<li class="px-2 py-2 text-2xl hover:underline bg-gray-200 w-full rounded">
			<a href="/">Home</a>
		</li>
		<li class="px-2 py-2 text-2xl hover:underline"><a href="/">Data</a></li>
		<li class="px-2 py-2 text-2xl hover:underline">
			<a href="https://github.com/MounirAia/Canadian-Tech-Salary-Prediction-App" target="_blank">
				Github Repo
			</a>
		</li>
		<li class="px-2 py-2 text-2xl hover:underline">
			<a href="mailto:m.bluth@example.com">Email</a>
		</li>
	</ul>
</aside>

<div class="min-h-screen w-full">
	<slot />
</div>

<footer class="w-full ml-64 h-40 grid grid-cols-10 gap-x-8 p-4 pl-8 border-t border-gray-300">
	<section class="contact col-span-2 flex flex-col gap-5">
		<h2 class="text-2xl font-medium">Contact</h2>
		<a class="text-base hover:underline" href="mailto:m.bluth@example.com">Email</a>
	</section>
	<section class="github col-span-2 flex flex-col gap-5">
		<h2 class="text-2xl font-medium">Github</h2>
		<a
			class="text-base hover:underline"
			href="https://github.com/MounirAia/Canadian-Tech-Salary-Prediction-App"
			target="_blank"
		>
			Github Repo
		</a>
	</section>
</footer>
