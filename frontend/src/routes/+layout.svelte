<script>
	import Heading from '$components/base/Heading.svelte';
	import '../app.css';
	import logo from '../assets/logo.png';
</script>

<header
	class="fixed top-0 z-20 flex flex-row items-center justify-start w-full h-12 gap-4 capitalize bg-white border-b md:pl-4 lg:ml-64 lg:pl-8"
>
	<Heading headingType="h1" customClass="hidden md:block">Free Palestine</Heading>

	<div class="flex flex-col flex-1 h-full">
		<div class="black w-full h-[33%] bg-black"></div>
		<div class="red-white w-full h-[33%]">
			<div class="red w-[30%] h-full bg-[#E4312b]"></div>
			<div class="white w-[70%] h-full bg-white"></div>
		</div>
		<div class="green w-full h-[35%] bg-[#149954]"></div>
	</div>
</header>

<aside class="fixed flex flex-col items-center w-64 h-full gap-5 border-r border-r-gray-300">
	<img src={logo} alt="Logo of the company" class="object-contain" />
	<ul class="flex flex-col w-full gap-4 px-2 text-left">
		<li class="w-full px-2 py-2 text-2xl bg-gray-200 rounded hover:underline">
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

<div class="min-h-screen mt-16 lg:ml-64">
	<slot />
</div>

<footer
	class="grid w-full h-40 grid-cols-2 p-4 pl-8 border-t border-gray-300 lg:ml-64 lg:grid-cols-10 gap-x-8"
>
	<section class="flex flex-col col-span-1 gap-5 contact lg:col-span-2">
		<h2 class="text-2xl font-medium">Contact</h2>
		<a class="text-base hover:underline" href="mailto:m.bluth@example.com">Email</a>
	</section>
	<section class="flex flex-col col-span-1 gap-5 github lg:col-span-2">
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
