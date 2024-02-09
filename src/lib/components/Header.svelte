<script>
	import '/src/app.css';
	import ThemeSelector from '$lib/theme-selector.svelte';
</script>

<!-- Logo Navbar space-->
<div class="navbar bg-gradient-to-r from-emerald-100 via-cyan-200 to-blue-200 flex-none md:w-auto justify-between items-center text-black overflow-x-auto">


	<div class="flex-none items-center">
	  <a href="/" class="btn btn-ghost text-xl text-pretty">
		<img src="/humanized6.jpg" width="50" height="50" alt="Logo" class="h-10"/>
		STATPAN</a>
	</div>
	<!-- Add a container div with responsive classes to wrap the search input and menu button -->
	
	<div class="flex items-center justify-end flex-auto">
		<!-- Add a responsive search input -->
	  <!-- theme controller -->
	  <div class="form-control max-w-18 mx-2 text-white">
		<input type="text" placeholder="Search" class="input input-bordered w-full max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg"/>
	  </div>
	  <ThemeSelector />
	  <button class="btn btn-square btn-ghost mr-2 flex-initial">
		<!-- Use an icon that indicates a menu, such as the hamburger icon -->
		<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-5 h-5 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16"></path></svg>
	  </button>
	</div>
	  
</div>
