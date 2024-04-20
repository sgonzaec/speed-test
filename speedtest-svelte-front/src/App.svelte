<script lang="ts">
  import Button from './lib/Button/Button.svelte';
  import Loader from './lib/Loader/Loader.svelte';
  import Table from './lib/Table/Table.svelte';
  import type { ResponseData } from './types';

  let isLoading = false;
  let isComplete = false;
  let responseData: ResponseData;

</script>

<main>

  <div class="card">
    {#if isLoading}
      <h1>Ejecutando...</h1>
      <Loader />
    {:else}
      <h1>Ejecutar prueba de velocidad</h1> 
      <Button bind:isLoading={isLoading} bind:isComplete={isComplete} bind:responseData={responseData}/>
    {/if}

    {#if isComplete}
      <Table bind:responseData={responseData} />
    {/if}
    
  </div>

</main>

<style>
  main .card{
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  h1 {
    margin: 0;
  }
</style>