<script setup lang="ts">

import { ref } from "vue"
import axios from 'axios'

const textInput = ref<string>("");
const numberInput = ref<number>(3);
const sizeInput = ref<number>(256);
const result = ref<string>("");
const loading = ref<boolean>(false);
const errorFlg = ref<boolean>(false);

const submitForm = async (): Promise<void> => {

  if (textInput.value.trim() !== "") {

    result.value = ""
    loading.value = true
    errorFlg.value = false

    const postData = {
      "prompt": textInput.value,
      "steps": numberInput.value,
      "size": sizeInput.value,
    }

    try {

      const response = await axios.post(
        'http://127.0.0.1:5000/api/image_generation',
        postData,
        {
          responseType: 'arraybuffer',
        }
      );
      const blob = new Blob([response.data], { type: 'image/jpeg' });
      const imageUrl = URL.createObjectURL(blob);
      result.value = imageUrl;

    } catch (error) {
      errorFlg.value = true
      console.error(error);
    }
    loading.value = false
  }

};

</script>

<template>

    <form>
        <div class="mt-4">
            <label for="exampleInput" class="form-label h2">英語を入力してください:</label>
            <input type="text" class="form-control" id="exampleInput" v-model="textInput">
        </div>
        <div class="mt-4">
            <label for="numberInput" class="form-label h4">Steps:</label>
            <input type="number" class="form-control" id="numberInput" v-model="numberInput">
        </div>
        <div class="mt-4">
            <label for="sizeInput" class="form-label h2">数字を選択してください:</label>
            <select class="form-select" id="sizeInput" v-model="sizeInput">
                <option value="256">256</option>
                <option value="512">512</option>
                <option value="1024">1024</option>
            </select>
        </div>
        <button type="button" class="btn btn-primary mt-3" @click="submitForm">Submit</button>
    </form>

    <div v-if="loading" class="mt-3">
      <p class="alert alert-dark d-flex align-items-center">
        <div class="spinner-border me-2 text-dark" role="status"></div>
          画像生成中
      </p>
    </div>

    <div v-if="errorFlg">
      画像の生成中にERRORが発生しました。
    </div>
    <div v-else-if="result" class="text-center">
      <div class="card w-25 mx-auto my-5">
        <div class="card-body">
          <h2 class="card-title">生成結果</h2>
        </div>
        <img class="img-fluid" v-bind:src="result" alt="Image">
      </div>
    </div>

</template>