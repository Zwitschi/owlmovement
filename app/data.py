"""
Centralized content data for the Corey Pellizzi website.
All dynamic content (projects, portfolio items, social links, metadata) is defined here.
"""

FEATURED_PROJECTS = [
    {
        "title": "Open Mic Odyssey",
        "description": "Three best friends embark on an outrageous adventure.",
        "image": "/static/images/thumbnail_for_odyssey.png",
        "link": "https://openmicodyssey.com/"
    },
    {
        "title": "Super Silly Show",
        "description": "Join Corky and Beefroast as they host a variety show like no other! Weekly comedy and entertainment.",
        "image": "/static/images/super-silly-show-logo.png",
        "link": "https://www.youtube.com/razzamatazzification"
    },
    {
        "title": "Owl Movement Music",
        "description": "Original music and soundscapes from the Corkyverse, available on multiple streaming platforms.",
        "image": "/static/images/corky-eye-pizza.gif",
        "link": "https://soundcloud.com/owl_movement"
    }
]

PORTFOLIO_ITEMS = [
    {
        "title": "Open Mic Odyssey",
        "categories": ["comedy", "video"],
        "description": "Three best friends embark on an outrageous adventure in this comedy sketch.",
        "image": "/static/images/thumbnail_for_odyssey.png",
        "link": "https://openmicodyssey.com/"
    },
    {
        "title": "Comedy Stains",
        "categories": ["comedy", "podcast"],
        "description": "Co-hosted podcast with Dave Sarra about comedy and humor",
        "image": "/static/images/comedy-stains-logo.jpg",
        "link": "https://anchor.fm/comedystains"
    },
    {
        "title": "Super Silly Sunday Show",
        "categories": ["comedy", "video"],
        "description": "Weekly variety show with Corky and Beefroast",
        "image": "/static/images/super-silly-show-logo.png",
        "link": "https://www.youtube.com/razzamatazzification"
    },
    {
        "title": "The Ding-Dong Show",
        "categories": ["video", "comedy"],
        "description": "Live show content and performances",
        "image": "/static/images/ding-dong-show-thumbnail.jpg",
        "link": "https://www.youtube.com/coreyowl"
    },
    {
        "title": "Owl Movement Collection",
        "categories": ["music"],
        "description": "Original compositions and soundscapes",
        "image": "/static/images/corky-eye-pizza.gif",
        "link": "https://soundcloud.com/owl_movement"
    },
    {
        "title": "Supersillyshow Music",
        "categories": ["music", "comedy"],
        "description": "Music from Corky Time and Super Silly Sunday Show on SoundCloud",
        "image": "/static/images/comedy-square-logo.png",
        "link": "https://soundcloud.com/supersillyshow"
    }
]

PROJECTS = [
    {
        "title": "Open Mic Odyssey",
        "type": "Documentary Film",
        "description": "Three best friends embark on an outrageous adventure.",
        "image": "/static/images/thumbnail_for_odyssey.png",
        "links": {
            "Official Site": "https://openmicodyssey.com/",
            "YouTube": "https://www.youtube.com/openmicodyssey",
            "Instagram": "https://www.instagram.com/openmicodyssey",
            "TikTok": "https://www.tiktok.com/@openmicodyssey",
        }
    },
    {
        "title": "Comedy Stains Podcast",
        "type": "Podcast",
        "description": "A podcast where two fully grown adults discuss the business and art of humor. Co-hosted with LA comedian Dave Sarra. Featuring deep dives into comedy, entertainment industry insights, and candid conversations about performing arts.",
        "image": "/static/images/comedy-stains-logo.jpg",
        "links": {
            "Anchor": "https://anchor.fm/comedystains",
            "YouTube": "https://www.youtube.com/channel/UCLwzUapNl8f2hQi6iflw_Gg",
            "SoundCloud": "https://soundcloud.com/comedystains",
            "Twitter": "https://www.twitter.com/ComedyStains",
            "Instagram": "https://www.instagram.com/ComedyStains",
            "Facebook": "https://www.facebook.com/ComedyStains/",
            "TikTok": "https://www.tiktok.com/@comedystains",
            "Twitch": "https://twitch.com/comedystains"
        }
    },
    {
        "title": "Super Silly Show",
        "type": "Variety Show",
        "description": "Join Corky and Beefroast as they host a variety show like no other! A weekly show featuring comedy, music, and entertainment. Available on multiple platforms including YouTube, Facebook, Twitter, Instagram, and SoundCloud.",
        "image": "/static/images/super-silly-show-logo.png",
        "links": {
            "YouTube": "https://www.youtube.com/razzamatazzification",
            "Facebook": "https://www.facebook.com/supersillyshow",
            "Twitter": "https://www.twitter.com/supersillyshow",
            "Instagram": "https://www.instagram.com/supersillysundayshow",
            "SoundCloud": "https://soundcloud.com/supersillyshow"
        }
    },
    {
        "title": "Original Music & Soundscapes",
        "type": "Music Production",
        "description": "Creating and releasing original music under the Owl Movement and Corky Time brands. Music is available across streaming platforms including SoundCloud, with new uploads from the Corkyverse regularly added.",
        "links": {
            "Owl Movement SoundCloud": "https://soundcloud.com/owl_movement",
            "Super Silly Show SoundCloud": "https://soundcloud.com/supersillyshow"
        }
    },
    {
        "title": "Comedy Videos & Content",
        "type": "Video Content",
        "description": "Comedy sketches, performances, and other video content available on YouTube. Features live shows, vlogs, interviews, and various entertainment media.",
        "image": "/static/images/ding-dong-show-thumbnail.jpg",
        "links": {
            "Main YouTube Channel": "https://www.youtube.com/coreyowl",
            "Corkytube": "https://www.youtube.com/user/Razzamatazzification"
        }
    },
    {
        "title": "Media & Gallery",
        "type": "Content Gallery",
        "description": "A collection of videos, comedy content, vlogs, interviews, music, and GIFs showcasing various projects and performances.",
        "links": {
            "Media Gallery": "https://owlmovement.wixsite.com/coreycomedy/media"
        }
    },
    {
        "title": "Merchandise & Shop",
        "type": "E-Commerce",
        "description": "Official merchandise store featuring print-to-order items and branded products.",
        "links": {
            "Corky Store": "https://corkstore.myspreadshop.com/",
            "Ko-Fi Support": "https://ko-fi.com/corky"
        }
    }
]

SOCIAL_MEDIA = {
    "Instagram": "https://instagram.com/owlmovement",
    "Twitter": "https://twitter.com/corkycomedynow",
    "Facebook": "https://facebook.com/corkycomedynow",
    "YouTube": "https://youtube.com/coreyowl",
    "SoundCloud": "https://soundcloud.com/owl_movement",
    "TikTok": "https://www.tiktok.com/@comedystains",
    "Twitch": "https://www.twitch.tv/officialbroadcast",
    "Ko-Fi": "https://ko-fi.com/corky"
}

PAGE_METADATA = {
    "index": {
        "title": "Corey Pellizzi - Comedian, Producer, Musician & Director",
        "description": "Welcome to the official website of Corey Pellizzi, a versatile entertainer and content creator. Explore comedy, music, podcasts, and creative projects.",
        "keywords": "comedian, comedy, producer, musician, director, writer, entertainment, Owl Movement, Comedy Stains",
        "og_title": "Corey Pellizzi - Home",
        "og_description": "Versatile entertainer and content creator featuring comedy, music, podcasts, and creative projects.",
        "og_image": "https://coreypellizzi.com/static/images/comedy-stains-logo.jpg",
        "og_url": "https://coreypellizzi.com/",
        "twitter_card": "summary_large_image",
        "twitter_creator": "@corkycomedynow",
        "canonical": "https://coreypellizzi.com/"
    },
    "bio": {
        "title": "About Corey Pellizzi - Biography & Expertise",
        "description": "Learn about Corey Pellizzi's journey as a comedian, producer, musician, director, and writer. Discover his expertise and recent creative projects.",
        "keywords": "about, biography, comedian, producer, musician, director, writer, Corey Pellizzi",
        "og_title": "About Corey Pellizzi",
        "og_description": "Discover the creative journey and expertise of Corey Pellizzi.",
        "og_image": "https://coreypellizzi.com/static/images/comedy-square-logo.png",
        "og_url": "https://coreypellizzi.com/bio",
        "twitter_card": "summary",
        "twitter_creator": "@corkycomedynow",
        "canonical": "https://coreypellizzi.com/bio"
    },
    "portfolio": {
        "title": "Portfolio - Comedy, Music, Video & Podcast Projects",
        "description": "Explore a comprehensive portfolio of comedy sketches, music, videos, podcasts, and blog content across multiple categories and platforms.",
        "keywords": "portfolio, comedy, music, video, podcast, projects, content, entertainment",
        "og_title": "Portfolio & Creative Works",
        "og_description": "Browse comedy, music, video, and podcast projects from Corey Pellizzi.",
        "og_image": "https://coreypellizzi.com/static/images/super-silly-show-logo.png",
        "og_url": "https://coreypellizzi.com/portfolio",
        "twitter_card": "summary_large_image",
        "twitter_creator": "@corkycomedynow",
        "canonical": "https://coreypellizzi.com/portfolio"
    },
    "projects": {
        "title": "Projects - Podcasts, Shows, Music & More",
        "description": "Discover featured projects including Comedy Stains Podcast, Super Silly Show, original music, video content, and merchandise.",
        "keywords": "projects, podcast, show, music, video, Comedy Stains, Super Silly Show, Owl Movement",
        "og_title": "Featured Projects",
        "og_description": "Explore Comedy Stains Podcast, Super Silly Show, and other creative projects.",
        "og_image": "https://coreypellizzi.com/static/images/comedy-stains-logo.jpg",
        "og_url": "https://coreypellizzi.com/projects",
        "twitter_card": "summary_large_image",
        "twitter_creator": "@corkycomedynow",
        "canonical": "https://coreypellizzi.com/projects"
    },
    "contact": {
        "title": "Contact - Get In Touch With Corey Pellizzi",
        "description": "Contact Corey Pellizzi for collaborations, inquiries, or support. Find social media links, merchandise, and multiple ways to connect.",
        "keywords": "contact, email, social media, collaboration, inquiries, support, Corey Pellizzi",
        "og_title": "Contact Corey Pellizzi",
        "og_description": "Get in touch with Corey Pellizzi for collaborations and inquiries.",
        "og_image": "https://coreypellizzi.com/static/images/comedy-square-logo.png",
        "og_url": "https://coreypellizzi.com/contact",
        "twitter_card": "summary",
        "twitter_creator": "@corkycomedynow",
        "canonical": "https://coreypellizzi.com/contact"
    }
}
