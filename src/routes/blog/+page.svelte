<script>
    import Body from "$lib/components/Body.svelte";
    import '/src/app.css';
    export let data;
</script>

<Body>
    <h1>Blog</h1>
    <ul>
        {#each data.summaries as { slug, title }}
		<li><a href="/blog/{slug}">{title}</a></li>
	    {/each}
    </ul>
</Body>