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
        <router-link :to="{ path: '/', hash: '#about' }">About</router-link>
        <router-link :to="{ path: '/', hash: '#skills' }">Skills</router-link>
        <router-link :to="{ path: '/', hash: '#projects' }">Projects</router-link>
        <router-link to="/digital-art">Digital Art</router-link>
        <router-link to="/games">Games</router-link>
        <router-link :to="{ path: '/', hash: '#guestbook' }">Guestbook</router-link>
        <router-link :to="{ path: '/', hash: '#contact' }">Contact</router-link>
        <button class="theme-toggle" @click="toggleTheme">
          {{ isDarkMode ? '☀️ Day' : '🌙 Night' }}
        </button>
      </div>
    </nav>

    <!-- Main Content rendered by Vue Router -->
    <main class="main">
      <router-view />
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
export default {
  name: 'App',
  data() {
    return {
      isDarkMode: false
    }
  },
  mounted() {
    // Check saved preference or system preference on load
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      this.isDarkMode = savedTheme === 'dark';
    } else {
      this.isDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
    }
    
    if (this.isDarkMode) {
      document.documentElement.classList.add('dark-mode');
    }
  },
  methods: {
    toggleTheme() {
      this.isDarkMode = !this.isDarkMode;
      
      if (this.isDarkMode) {
        document.documentElement.classList.add('dark-mode');
        localStorage.setItem('theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark-mode');
        localStorage.setItem('theme', 'light');
      }
    }
  }
}
</script>