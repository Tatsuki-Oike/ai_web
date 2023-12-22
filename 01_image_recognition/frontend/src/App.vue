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

const handleSubmit = async (): Promise<void> => {

  if (file.value) {

    result.value = ""
    loading.value = true
    errorFlg.value = false
    
    const formData = new FormData();
    formData.append('image', file.value);

    try {

      const response = await axios.post(
        'http://127.0.0.1:5000/api/image_recognition', 
        formData, 
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }
      );

      result.value = response.data
      console.log(response.data);

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
        画像認識中
      </p>
    </div>

    <div v-if="errorFlg">
      画像認識でERRORが発生しました。
    </div>
    <div v-else-if="result">
      {{ result }}
    </div>

</template>

