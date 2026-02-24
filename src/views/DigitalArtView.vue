<template>
  <div class="digital-art-page">
    <!-- Title: Digital Art Gallery -->
    <!-- Description: A separate page to showcase digital artwork. Add new art pieces to the artImages array below. -->
    
    <section id="digital-art" class="section">
      <div class="container">
        <h2>Digital Art</h2>
        <div class="art-gallery">
          <div class="art-item" v-for="(art, index) in artImages" :key="index" @click="openModal(art.path)">
            <img :src="art.path" :alt="art.alt" class="clickable-image" />
          </div>
        </div>
      </div>
    </section>

    <!-- Fullscreen Image Modal -->
    <div v-if="selectedImage" class="image-modal" @click="closeModal">
      <button class="close-btn" @click.stop="closeModal">&times;</button>
      <img :src="selectedImage" alt="Fullscreen Art" class="modal-content" @click.stop />
    </div>
  </div>
</template>

<script>
export default {
  name: 'DigitalArtView',
  data() {
    return {
      artImages: [
        { path: '/images/art/ARTPRE1.jpg', alt: 'Digital Art 1' },
        { path: '/images/art/Bladerunner2049.jpg', alt: 'Digital Art 2' },
        { path: '/images/art/wallpaper.png', alt: 'Digital Art 3' },
        { path: '/images/art/zumba.jpg', alt: 'Fitness Circuit Creation' },
          { path: '/images/art/Travis Minimized.png', alt: 'Travis Minimized' },
        { path: '/images/art/Hornet in The alps.jpg', alt: 'Hornet in The Alps' }
      ],
      selectedImage: null
    }
  },
  methods: {
    openModal(imagePath) {
      this.selectedImage = imagePath;
      document.body.style.overflow = 'hidden'; // Prevent scrolling when modal is open
    },
    closeModal() {
      this.selectedImage = null;
      document.body.style.overflow = 'auto'; // Re-enable scrolling
    }
  }
}
</script>
