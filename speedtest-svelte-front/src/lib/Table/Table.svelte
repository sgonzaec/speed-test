<script lang="ts">
  import type { ResponseData } from "../../types";

  export let responseData: ResponseData;
</script>

<div class="content">
  <div class="main">
    <div class="child">
      <p>Carga</p>
      <p>{responseData.upload}</p>
    </div>
    <div class="child">
      <p>Descarga</p>
      <p>{responseData.download}</p>
    </div>
    <div class="child">
      <p>Latencia</p>
      <p>{responseData.latency}</p>
    </div>
  </div>
  <div class="main">
    <div class="child">
      <p>Ping</p>
      <p>{responseData.ping}</p>
    </div>
    <div class="child">
      <p>Proveedor</p>
      <p>{responseData.sponsor}</p>
    </div>
    <div class="child">
      <p>Host</p>
      <p>{responseData.host}</p>
    </div>
  </div>
</div>

<style>
  .content {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .main {
    display: flex;
    gap: 20px;
    justify-content: space-between;
  }
  .child {
    border: 1px dotted gray;
    padding: 0.5em 1em;
    border-radius: 15px;
  }
</style>
