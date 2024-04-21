<script lang="ts">
  import type { ResponseData } from "../../types";

  export let responseData: ResponseData;
</script>

<div class="content">
  <div class="main">
    <div class="child">
      <p>Carga &#9195;</p>
      <p>{responseData.upload}</p>
    </div>
    <div class="child">
      <p>Descarga &#9196;</p>
      <p>{responseData.download}</p>
    </div>
    <div class="child">
      <p>Latencia &#9203;</p>
      <p>{responseData.latency}</p>
    </div>
  </div>
  <div class="main">
    <div class="child">
      <p>Ping &#10071;</p>
      <p>{responseData.ping}</p>
    </div>
    <div class="child">
      <p>Proveedor &#128666;</p>
      <p>{responseData.sponsor}</p>
    </div>
    <div class="child">
      <p>Host &#127970;</p>
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
  @media only screen and (max-width: 768) {
    .main {
      flex-direction: column;
    }
  }
  .child {
    background-color: rgba(255, 255, 255, 0.2);
    box-shadow: rgba(255, 255, 255, 0.1) 0px 4px 12px;
    padding: 0.5em 1em;
    border-radius: 15px;
  }
</style>
