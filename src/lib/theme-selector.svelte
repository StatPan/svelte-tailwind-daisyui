<script lang="ts">
	import { onMount } from 'svelte';
	import themes from './themes/themes';
	import { basic_themes } from './themes/themes';


	export let currentTheme = "night"
	export let Theme1 = "cupcake"
	export let Theme2 = "night"
	onMount(() => {
		if (typeof window !== 'undefined') {
			const theme = window.localStorage.getItem('theme')
			if (theme && themes.includes(theme)) {
				document.documentElement.setAttribute('data-theme', theme)
				currentTheme = theme
			}
		}
	})

	function set_theme(theme: string) {
		const one_year = 60 * 60 * 24 * 365
		window.localStorage.setItem('theme', theme)
		document.cookie = `theme=${theme}; max-age=${one_year}; path=/; SameSite=Lax`
		document.documentElement.setAttribute('data-theme', theme)
	}

	const handleTheme = (): void => currentTheme === Theme1 ? set_theme(currentTheme = Theme2) : set_theme(currentTheme = Theme1);


</script>

<label class="flex cursor-pointer gap-2">
	<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>
	<input bind:value={currentTheme} on:click={handleTheme} type="checkbox" class="toggle theme-controller"/>
	<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
</label>