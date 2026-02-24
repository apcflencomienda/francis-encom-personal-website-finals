<template>
  <div class="home">
    <!-- About Section (Wiki Style) -->
    <section id="about" class="section">
      <div class="container">
        <h2>About Me</h2>
        
        <div class="wiki-layout">
          <!-- Left Column: Main Description & Goals -->
          <div class="wiki-main">
            <p>Hello! I'm Francis Frederick L. Encomienda, a BSCS-SS231 student passionate about technology, digital art, and gaming. 
              I enjoy creating digital artwork and working on programming projects.</p>
          </div>
          
          <!-- Right Column: Wiki Infobox -->
          <aside class="wiki-infobox">
            <div class="infobox-header">About site author</div>
            <table class="infobox-table">
              <tbody>
                <tr>
                  <th scope="row"></th>
                  <td>Age (23)<br>Quezon City</td>
                </tr>
                <tr>
                  <th scope="row">Education</th>
                  <td>
                    <strong>Asia Pacific College</strong><br>
                    BS Computer Science (Current)<br><br>
                    <strong>Senior High School (2021)</strong><br>
                    ABM Strand<br>
                    Accounting, Business Management Specializing in Management
                  </td>
                </tr>
                <tr>
                  <th scope="row">Aliases</th>
                  <td>Flencomienda<br>Encom<br>Friedrich<br>Cedric<br>Cedy<br>Ced<br>Cd<br>Magic Wand</td>
                </tr>
              </tbody>
            </table>
          </aside>
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
          <p>Email: <a href="#" class="placeholder-link">@flencomienda@student.apc.edu</a></p>
          <p>GitHub: <a href="https://github.com/apcflencomienda" target="_blank" class="link">github.com/apcflencomienda</a></p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

export default {
  name: 'HomeView',
  data() {
    return {
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
