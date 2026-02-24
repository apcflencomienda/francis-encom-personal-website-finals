<template>
  <div class="games-page">
    <!-- Title: Games Section -->
    <!-- Description: A separate page dedicated to favorite games. Add or remove items in the gameImages array below. -->
    
    <section id="games" class="section">
      <div class="container">
        <h2>Favorite Games</h2>
        <div class="games-grid">
          <div class="game-card" v-for="(game, index) in gameImages" :key="index" @click="openModal(game.path)">
            <img :src="game.path" :alt="game.alt" class="clickable-image" />
            <p class="game-desc">{{ game.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Fullscreen Image Modal -->
    <div v-if="selectedImage" class="image-modal" @click="closeModal">
      <button class="close-btn" @click.stop="closeModal">&times;</button>
      <img :src="selectedImage" alt="Fullscreen Game" class="modal-content" @click.stop />
    </div>
  </div>
</template>

<script>
export default {
  name: 'GamesView',
  data() {
    return {
      gameImages: [
        { path: '/images/games/bf1.png', alt: 'Battlefield 1', desc: 'A beautiful WW1 simulator where you spend 90% of your time dying to a guy spamming the artillery truck from his spawn point.' },
        { path: '/images/games/city_skylines.png', alt: 'Cities Skylines', desc: 'The ultimate "why is my traffic 100% red" simulator. Your citizens will literally drink their own sewage before figuring out how to use a 4-lane roundabout.' },
        { path: '/images/games/project_reality.png', alt: 'Project Reality', desc: 'A tactical military game for people who think walking 5 kilometers across an empty desert just to get shot by an unseen sniper is fun.' },
        { path: '/images/games/war_thunder.png', alt: 'War Thunder', desc: 'A classified military documents leak disguised as a game where you grind for thousands of hours just to suffer from Russian bias.' },
        { path: '/images/games/zzz.png', alt: 'ZZZ Game', desc: 'A perfectly crafted strategy to drain your wallet and sanity disguised as a high-action Gacha game. May RNG be ever in your favor.' }
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
