<script setup lang="ts">

import { ref } from "vue"
import axios from 'axios'

const file = ref<File | null>(null);
const result = ref<string>("");
const loading = ref<boolean>(false);
const errorFlg = ref<boolean>(false);

const handleFileChange = (event: Event): void => {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files.length > 0) {
    file.value = input.files[0];
  }
};

const handleSubmit = async () => {

  if (file.value) {
    result.value = ""
    loading.value = true
    errorFlg.value = false

    const formData = new FormData();
    formData.append('image', file.value);

    try {

      const response = await axios.post(
        'http://127.0.0.1:5000/api/segmentation', 
        formData, 
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

    <form @submit.prevent="handleSubmit" class="my-4">

      <div class="my-3">
        <label for="fileInput" class="form-label display-6"> 画像のアップロード </label>
        <input type="file" id="fileInput" ref="fileInput" 
          class="form-control form-control-lg mt-3" @change="handleFileChange">
      </div>

      <button type="submit" class="btn btn-primary btn-lg w-100">Submit</button>
    </form>

    <div v-if="loading" class="mt-3">
      <p class="alert alert-dark d-flex align-items-center">
        <div class="spinner-border me-2 text-dark" role="status"></div>
          セグメンテーションを行っています
      </p>
    </div>

    <div v-if="errorFlg">
      セグメンテーション中にERRORが発生しました。
    </div>
    <div v-else-if="result" class="text-center">
      <div class="card w-25 mx-auto my-5">
        <div class="card-body">
          <h2 class="card-title">切り抜き結果</h2>
        </div>
        <img class="img-fluid" v-bind:src="result" alt="Image">
      </div>
    </div>

</template>

