<script>
	import Header from '$lib/components/Header.svelte'
	import Navbar from '$lib/components/Navbar.svelte'
	import Footer from '$lib/components/Footer.svelte'
	import Body from '$lib/components/Body.svelte';
</script>


<div class="w-full flex flex-col">

<Header />

<Navbar />

<Body>
	<slot></slot>
</Body>

<Footer />

</div>