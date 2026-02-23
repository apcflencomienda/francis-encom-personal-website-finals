<template>
  <div id="app">
    <!-- Header with circular profile picture -->
    <header class="header">
      <div class="container">
        <h1>Francis Frederick L. Encomienda</h1>
        <p class="subtitle">BSCS-SS231 Student</p>
        
        <!-- Circular Profile Picture -->
        <div class="profile-container">
          <img 
            src="/images/profile/20210620_103703.jpg" 
            alt="Francis Encomienda" 
            class="profile-pic"
          />
        </div>
      </div>
    </header>

    <!-- Navigation -->
    <nav class="nav">
      <div class="container">
        <a href="#about" @click="scrollToSection('about')">About</a>
        <a href="#skills" @click="scrollToSection('skills')">Skills</a>
        <a href="#projects" @click="scrollToSection('projects')">Projects</a>
        <a href="#digital-art" @click="scrollToSection('digital-art')">Digital Art</a>
        <a href="#games" @click="scrollToSection('games')">Games</a>
        <a href="#guestbook" @click="scrollToSection('guestbook')">Guestbook</a>
        <a href="#contact" @click="scrollToSection('contact')">Contact</a>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="main">
      <!-- About Section -->
      <section id="about" class="section">
        <div class="container">
          <h2>About Me</h2>
          <div class="about-content">
            <p>Hello! I'm Francis Frederick L. Encomienda, a BSCS-SS231 student passionate about technology, digital art, and gaming. I enjoy creating digital artwork and working on programming projects.</p>
          </div>
        </div>
      </section>

      <!-- Skills Section -->
      <section id="skills" class="section">
        <div class="container">
          <h2>Skills</h2>
          <div class="skills-grid">
            <div class="skill-card">Digital Art</div>
            <div class="skill-card">Photo Editing</div>
            <div class="skill-card">Web Development</div>
            <div class="skill-card">Graphic Design</div>
          </div>
        </div>
      </section>

      <!-- Projects Section -->
      <section id="projects" class="section">
        <div class="container">
          <h2>Projects</h2>
          <div class="project-card">
            <h3>AGHAMazingQuest CMS</h3>
            <p>An APC-DOST Project - A content management system for educational purposes.</p>
          </div>
        </div>
      </section>

      <!-- Digital Art Section -->
      <section id="digital-art" class="section">
        <div class="container">
          <h2>Digital Art</h2>
          <div class="art-gallery">
            <div class="art-item" v-for="(art, index) in artImages" :key="index">
              <img :src="art.path" :alt="art.alt" />
            </div>
          </div>
        </div>
      </section>

      <!-- Games Section -->
      <section id="games" class="section">
        <div class="container">
          <h2>Favorite Games</h2>
          <div class="games-grid">
            <div class="game-card" v-for="(game, index) in gameImages" :key="index">
              <img :src="game.path" :alt="game.alt" />
            </div>
          </div>
        </div>
      </section>

      <!-- Guestbook Section -->
      <section id="guestbook" class="section">
        <div class="container">
          <h2>Guestbook</h2>
          <p class="guestbook-subtitle">Leave a message!</p>

          <!-- Submit Form (POST) -->
          <form class="guestbook-form" @submit.prevent="submitComment">
            <input
              v-model="newComment.name"
              type="text"
              placeholder="Your name"
              class="guestbook-input"
              required
            />
            <textarea
              v-model="newComment.message"
              placeholder="Your message..."
              class="guestbook-textarea"
              rows="3"
              required
            ></textarea>
            <button type="submit" class="guestbook-btn" :disabled="submitting">
              {{ submitting ? 'Sending...' : 'Leave a Message' }}
            </button>
          </form>

          <!-- Success / Error feedback -->
          <p v-if="submitSuccess" class="feedback success">✅ Message sent! Thank you!</p>
          <p v-if="submitError" class="feedback error">❌ Something went wrong. Please try again.</p>

          <!-- Comments List (GET) -->
          <div class="comments-list">
            <p v-if="loadingComments" class="loading-text">Loading messages...</p>
            <p v-else-if="comments.length === 0" class="no-comments">No messages yet. Be the first!</p>
            <div v-else class="comment-card" v-for="comment in comments" :key="comment.id">
              <div class="comment-header">
                <span class="comment-name">{{ comment.name }}</span>
                <span class="comment-date">{{ formatDate(comment.created_at) }}</span>
              </div>
              <p class="comment-message">{{ comment.message }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Contact Section -->
      <section id="contact" class="section">
        <div class="container">
          <h2>Contact</h2>
          <div class="contact-info">
            <p>Email: <a href="#" class="placeholder-link">Coming Soon</a></p>
            <p>GitHub: <a href="https://github.com/apcflencomienda" target="_blank" class="link">github.com/apcflencomienda</a></p>
          </div>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <p>&copy; 2025 Francis Encomienda. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script>
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

export default {
  name: 'App',
  data() {
    return {
      artImages: [
        { path: '/images/art/ARTPRE1.jpg', alt: 'Digital Art 1' },
        { path: '/images/art/Bladerunner2049.jpg', alt: 'Digital Art 2' },
        { path: '/images/art/wallpaper.png', alt: 'Digital Art 3' }
      ],
      gameImages: [
        { path: '/images/games/bf1.png', alt: 'Battlefield 1' },
        { path: '/images/games/city_skylines.png', alt: 'Cities Skylines' },
        { path: '/images/games/project_reality.png', alt: 'Project Reality' },
        { path: '/images/games/war_thunder.png', alt: 'War Thunder' },
        { path: '/images/games/zzz.png', alt: 'ZZZ Game' }
      ],
      // Guestbook data
      comments: [],
      loadingComments: false,
      newComment: {
        name: '',
        message: ''
      },
      submitting: false,
      submitSuccess: false,
      submitError: false
    }
  },
  mounted() {
    this.fetchComments()
  },
  methods: {
    scrollToSection(sectionId) {
      const element = document.getElementById(sectionId)
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
      }
    },

    // GET - Fetch all comments from Flask backend
    async fetchComments() {
      this.loadingComments = true
      try {
        const response = await fetch(`${API_URL}/comments`)
        if (!response.ok) throw new Error('Failed to fetch')
        this.comments = await response.json()
      } catch (error) {
        console.error('Error fetching comments:', error)
      }
      this.loadingComments = false
    },

    // POST - Submit a new comment to Flask backend
    async submitComment() {
      this.submitting = true
      this.submitSuccess = false
      this.submitError = false

      try {
        const response = await fetch(`${API_URL}/comments`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name: this.newComment.name, message: this.newComment.message })
        })
        if (!response.ok) throw new Error('Failed to submit')
        this.submitSuccess = true
        this.newComment.name = ''
        this.newComment.message = ''
        await this.fetchComments()
      } catch (error) {
        console.error('Error submitting comment:', error)
        this.submitError = true
      }

      this.submitting = false

      // Hide feedback after 3 seconds
      setTimeout(() => {
        this.submitSuccess = false
        this.submitError = false
      }, 3000)
    },

    formatDate(dateString) {
      const date = new Date(dateString)
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    }
  }
}
</script>