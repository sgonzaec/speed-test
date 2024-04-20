<script>
  export let isLoading;
  export let isComplete;
  export let responseData;
  

  async function fetchData() {
    isLoading = true;
    isComplete = false;
    try {
      const response = await fetch("http://127.0.0.1:5000/speed-test");
      if (!response.ok) {
        isLoading = false;
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      responseData = data;
      isComplete = true;
      isLoading = false;
    } catch (error) {
      console.error("Error fetching data:", error);
      isLoading = false;
    }
  }
</script>

<button class="btn-1" on:click={fetchData}>
  <p>Ejecutar prueba</p>
</button>

<style>
  .btn-1 {
    margin: 2em;
    width: 80%;
  }
</style>
