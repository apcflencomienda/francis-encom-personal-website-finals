import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DigitalArtView from '../views/DigitalArtView.vue'
import GamesView from '../views/GamesView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/digital-art',
            name: 'digital-art',
            component: DigitalArtView,
        },
        {
            path: '/games',
            name: 'games',
            component: GamesView,
        }
    ],
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        }

        // If the route has a hash (like /#about), scroll to it
        if (to.hash) {
            return {
                el: to.hash,
                behavior: 'smooth',
            }
        }

        // Default to top of the page
        return { top: 0 }
    },
})

export default router
