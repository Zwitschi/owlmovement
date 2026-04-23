# Owlmovement website

This is the repository for the Owlmovement website.

## Table of Contents

- [Owlmovement website](#owlmovement-website)
  - [Table of Contents](#table-of-contents)
  - [Target Content](#target-content)
    - [Discovered Pages](#discovered-pages)
    - [Page-Specific Content](#page-specific-content)
      - [Home Page](#home-page)
      - [Music Page](#music-page)
      - [Projects Page](#projects-page)
      - [MSG CORKY (Chat)](#msg-corky-chat)
      - [Merch Page](#merch-page)
      - [Media Page](#media-page)
      - [Mystery (???)](#mystery-)
      - [Super Silly Show](#super-silly-show)
      - [Blog Page](#blog-page)
      - [Comedy Stains](#comedy-stains)
    - [Images and Media URLs](#images-and-media-urls)
      - [Logo and Branding](#logo-and-branding)
      - [Blog Post Images](#blog-post-images)
      - [YouTube Thumbnails](#youtube-thumbnails)
    - [External Social Media Links](#external-social-media-links)
  - [Templating](#templating)
    - [Template Structure](#template-structure)
    - [Template Variables](#template-variables)
    - [Usage](#usage)
  - [Flask Application](#flask-application)
    - [Project Structure](#project-structure)
    - [Configuration](#configuration)
    - [Routes](#routes)
    - [Running the Application](#running-the-application)
    - [Data Management](#data-management)
    - [Static Assets](#static-assets)
  - [Content Population](#content-population)
    - [Content Discovery \& Mapping](#content-discovery--mapping)
    - [Image \& Media Handling](#image--media-handling)
    - [Social Media Integration](#social-media-integration)
    - [Implementation Challenges \& Solutions](#implementation-challenges--solutions)
    - [Data Structure](#data-structure)
    - [Content Updates](#content-updates)
  - [Image Management](#image-management)
    - [Local Image Storage](#local-image-storage)
    - [Image URL Mapping](#image-url-mapping)
    - [Downloading Images](#downloading-images)
    - [Image Files Updated](#image-files-updated)
    - [Benefits of Local Image Storage](#benefits-of-local-image-storage)
  - [Metadata and SEO](#metadata-and-seo)
    - [Metadata Structure](#metadata-structure)
    - [Page Metadata](#page-metadata)
      - [Home Page (`/`)](#home-page-)
      - [Biography Page (`/bio`)](#biography-page-bio)
      - [Portfolio Page (`/portfolio`)](#portfolio-page-portfolio)
      - [Projects Page (`/projects`)](#projects-page-projects)
      - [Contact Page (`/contact`)](#contact-page-contact)
    - [Meta Tags Implemented](#meta-tags-implemented)
      - [Standard Meta Tags](#standard-meta-tags)
      - [Open Graph Tags (Facebook, LinkedIn, Pinterest)](#open-graph-tags-facebook-linkedin-pinterest)
      - [Twitter Card Tags (Twitter-specific optimization)](#twitter-card-tags-twitter-specific-optimization)
    - [Implementation](#implementation)
    - [Template Rendering](#template-rendering)
    - [SEO Benefits](#seo-benefits)
    - [Updating Metadata](#updating-metadata)
    - [Best Practices](#best-practices)
  - [Testing](#testing)
    - [Test Suite Overview](#test-suite-overview)
    - [Test Organization](#test-organization)
      - [1. **TestRoutes** (8 tests)](#1-testroutes-8-tests)
      - [2. **TestMetadata** (7 tests)](#2-testmetadata-7-tests)
      - [3. **TestImageEmbedding** (3 tests)](#3-testimageembedding-3-tests)
      - [4. **TestPageContent** (5 tests)](#4-testpagecontent-5-tests)
      - [5. **TestNavigation** (3 tests)](#5-testnavigation-3-tests)
      - [6. **TestHTML** (4 tests)](#6-testhtml-4-tests)
      - [7. **TestResponseHeaders** (2 tests)](#7-testresponseheaders-2-tests)
      - [8. **TestFormValidation** (3 tests)](#8-testformvalidation-3-tests)
    - [Running Tests](#running-tests)
      - [Install Test Dependencies](#install-test-dependencies)
      - [Run All Tests](#run-all-tests)
      - [Run Specific Test Class](#run-specific-test-class)
      - [Run Specific Test](#run-specific-test)
      - [Run with Coverage Report](#run-with-coverage-report)
      - [Run Tests Quietly (Summary Only)](#run-tests-quietly-summary-only)
      - [Run Tests with Detailed Output](#run-tests-with-detailed-output)
    - [Test Fixtures](#test-fixtures)
    - [Test Configuration](#test-configuration)
    - [What Gets Tested](#what-gets-tested)
    - [Test Results](#test-results)
    - [Test Coverage Metrics](#test-coverage-metrics)
    - [Best Practices for Testing](#best-practices-for-testing)
    - [Troubleshooting Tests](#troubleshooting-tests)
    - [Continuous Integration](#continuous-integration)
  - [Static HTML Generation](#static-html-generation)
    - [Static Site Generation](#static-site-generation)
    - [Running Static Generation](#running-static-generation)
      - [Generate Static Site](#generate-static-site)
      - [Output](#output)
    - [Serving the Static Site Locally](#serving-the-static-site-locally)
      - [Using Python's Built-in Server](#using-pythons-built-in-server)
      - [Using Node.js http-server](#using-nodejs-http-server)
      - [Using Live Server (VS Code)](#using-live-server-vs-code)
    - [Deploying Static Site](#deploying-static-site)
      - [GitHub Pages](#github-pages)
      - [Netlify](#netlify)
      - [AWS S3 + CloudFront](#aws-s3--cloudfront)
      - [Vercel](#vercel)
      - [Traditional Web Hosting](#traditional-web-hosting)
    - [Generation Process](#generation-process)
    - [Generated File Analysis](#generated-file-analysis)
    - [Performance Benefits](#performance-benefits)
    - [Example Workflow](#example-workflow)
    - [Static Site vs Flask Application](#static-site-vs-flask-application)
    - [Troubleshooting](#troubleshooting)
    - [Next Steps](#next-steps)

## Target Content

This section documents all discovered content from the Corey Pellizzi website crawl.

### Discovered Pages

1. **Home Page** - https://owlmovement.wixsite.com/coreycomedy
2. **Music** - https://owlmovement.wixsite.com/coreycomedy/music
3. **Projects** - https://owlmovement.wixsite.com/coreycomedy/projects
4. **MSG CORKY (Chat)** - https://owlmovement.wixsite.com/coreycomedy/corky-chat
5. **Merch** - https://owlmovement.wixsite.com/coreycomedy/merch
6. **Media** - https://owlmovement.wixsite.com/coreycomedy/media
7. **Mystery (???)** - https://owlmovement.wixsite.com/coreycomedy/mystery
8. **Super Silly Show** - https://owlmovement.wixsite.com/coreycomedy/supersillyshow
9. **Blog** - https://owlmovement.wixsite.com/coreycomedy/blog
10. **Comedy Stains (Podcast)** - https://owlmovement.wixsite.com/coreycomedy/comedystains

### Page-Specific Content

#### Home Page

- Navigation menu with links to all pages
- Branding and introduction
- Social media links
- Ko-Fi donation link

#### Music Page

- Link to "Music from Corky Time and Super Silly Sunday Show" SoundCloud: https://soundcloud.com/supersillyshow
- Link to "Owl Movement" SoundCloud: https://soundcloud.com/owl_movement

#### Projects Page

**Sections:**

- FILM
- LIVE (The Ding-dong show with YouTube thumbnail)
- TALK / COMEDY STAINS (Podcast link)
- OTHER APPEARANCES

#### MSG CORKY (Chat)

- Interactive chat interface (content details not fully captured)

#### Merch Page

- PRINT TO ORDER section linking to: https://corkstore.myspreadshop.com/
- BRAND MERCH section (under construction)

#### Media Page

**Sections:**

- VIDS (Videos section)
- Comedy (comedy videos)
- VLOGS • INTERVIEWS • OTHER
- MUSIC
- GIFS

#### Mystery (???)

- Easter egg page with hidden content

#### Super Silly Show

- Logo and branding
- Description: "Join Corky and Beefroast as they host a variety show like no other!"
- Social media links:
  - Facebook: https://www.facebook.com/supersillyshow
  - Twitter: https://www.twitter.com/supersillyshow
  - YouTube: https://www.youtube.com/c/SimplyDonThePodcastNetworkYoutube
  - Instagram: https://www.instagram.com/supersillysundayshow
  - SoundCloud: https://soundcloud.com/supersillyshow

#### Blog Page

**Recent Posts:**

- "Getting caught up" - July 9, 2022 (mentions SoundCloud uploads)
- "The Stains of Comedy" - April 14, 2021 (mentions podcast with LA comedian Dave Sarra)
- "New Beginnings and Old Endings" - March 5, 2021

#### Comedy Stains

**Description:** A show where two fully grown adults discuss the business and art of humor.
**Official Accounts:**

- YouTube: https://www.youtube.com/channel/UCLwzUapNl8f2hQi6iflw_Gg
- Anchor: https://anchor.fm/comedystains
- Twitter: https://www.twitter.com/ComedyStains
- Instagram: https://www.instagram.com/ComedyStains
- Facebook: https://www.facebook.com/ComedyStains/
- SoundCloud: https://soundcloud.com/comedystains
- TikTok: https://www.tiktok.com/@comedystains?lang=en
- Twitch: https://twitch.com/comedystains

**Hosts:**

- Corky (Twitter: https://www.twitter.com/CorkyComedyNow, Instagram: https://www.instagram.com/OwlMovement)
- Dave (Twitter: https://twitter.com/DaveXHALE, Instagram: https://www.instagram.com/Dave.Sarra, YouTube: http://www.youtube.com/DaveSarra, Twitch: https://www.twitch.tv/davesarra)

### Images and Media URLs

#### Logo and Branding

1. **Corky's eye and pizza** (GIF) - https://static.wixstatic.com/media/11d46c_b97cf97a3e754c13a503e2fd6b800264~mv2.gif
2. **Corkster biz website logo** (PNG) - https://static.wixstatic.com/media/11d46c_8508e60b07bf46e3a5a386987aa88529~mv2.png
3. **Comedy square logo** (PNG) - https://static.wixstatic.com/media/11d46c_f2cffe20d5b848c18163074c0754629b~mv2.png
4. **Comedy stains logo banner** (JPG) - https://static.wixstatic.com/media/11d46c_7439f513351e479c89cb129a9002d411~mv2.jpg
5. **Super silly sunday show logo** (PNG) - https://static.wixstatic.com/media/11d46c_4edf89bfd02243b0886637a41c35169b~mv2.png
6. **Site under construction** (PNG) - https://static.wixstatic.com/media/11d46c_2aba38e93309499b8e5fa34dc2695de5~mv2.png

#### Blog Post Images

7. **Getting caught up** (JPG) - https://static.wixstatic.com/media/11d46c_894b8abbce22443187515709a2dedb9c~mv2.jpg
8. **The Stains of Comedy** (PNG) - https://static.wixstatic.com/media/11d46c_62f309fab95b43b595aa234703f56bfe~mv2.png
9. **New Beginnings and Old Endings** (JPG) - https://static.wixstatic.com/media/11d46c_4d823c329744484bb8b092480ed44cad~mv2.jpg

#### YouTube Thumbnails

10. **The Ding-dong show** (JPG) - https://yt3.ggpht.com/ytc/AIdro_kTv0bX_37Lqi2_K13_b3b5hMMgsx35Hzfe__5GQjwCey0=s800-c-k-c0x00ffffff-no-rw

### External Social Media Links

- Instagram: https://instagram.com/owlmovement
- Twitter: https://twitter.com/corkycomedynow
- Facebook: https://facebook.com/corkycomedynow
- YouTube (Coreyowl): https://youtube.com/coreyowl
- YouTube (Corkytube): https://www.youtube.com/user/Razzamatazzification
- IMDB: https://www.imdb.com/name/nm3869184/
- Twitch: https://www.twitch.tv/officialbroadcast
- Periscope: https://www.periscope.tv/coreyowl/
- SoundCloud: https://soundcloud.com/owl_movement
- StoryFire: https://storyfire.app.link/LAynRlWXg7
- Firework TV: https://fireworktv.com/ch/owlmovement

## Templating

The website uses **Jinja2 templates** to create dynamic HTML pages. The templating system is organized hierarchically with a base template that all pages inherit from.

### Template Structure

**Base Template** (`app/templates/base.html`)

- Contains the overall HTML structure (DOCTYPE, head, body)
- Defines the navigation bar with links to all pages
- Provides the footer with social media links
- Uses `{% block content %}` to allow child templates to inject page-specific content
- Automatically includes CSS and JavaScript resources

**Child Templates**
Each page extends the base template and provides its own content:

1. **index.html** - Home/landing page
   - Hero section with call-to-action buttons
   - Featured projects grid
   - Collaboration call-to-action section

2. **bio.html** - Biography page
   - Personal biography section
   - Expertise list
   - Recent projects overview

3. **portfolio.html** - Portfolio showcase
   - Portfolio items grid with filtering
   - Category filters (All, Comedy, Music, Video, Podcast)
   - Hover effects to view projects

4. **projects.html** - Projects details
   - Detailed project descriptions
   - Links to external platforms
   - Featured shows and collaborations section

5. **contact.html** - Contact form
   - Contact form with validation
   - Social media links
   - Support/donation links

### Template Variables

Templates have access to the following variables passed from Flask routes:

- `title` - Page title for the HTML head tag
- `featured_projects` - List of featured project objects
- `portfolio_items` - List of portfolio items with filtering metadata
- `projects` - List of detailed project information
- `social_media` - Dictionary of social media platform URLs

### Usage

To create a new page:

1. Create a new `.html` file in `app/templates/`
2. Start with: `{% extends "base.html" %}`
3. Define content block: `{% block content %} ... {% endblock %}`
4. Create a Flask route to render the template
5. Pass required variables from the route

Example:

```jinja2
{% extends "base.html" %}

{% block content %}
<section class="page-section">
    <div class="container">
        <h1>{{ page_title }}</h1>
        <!-- Your content here -->
    </div>
</section>
{% endblock %}
```

## Flask Application

The website is built using **Flask**, a lightweight Python web framework. The application serves dynamic content and handles routing.

### Project Structure

```
owlmovement/
├── app/
│   ├── templates/          # Jinja2 HTML templates
│   │   ├── base.html       # Base template
│   │   ├── index.html      # Home page
│   │   ├── bio.html        # Biography page
│   │   ├── portfolio.html  # Portfolio page
│   │   ├── projects.html   # Projects page
│   │   └── contact.html    # Contact page
│   └── static/             # Static assets
│       ├── css/
│       │   └── style.css   # Main stylesheet
│       ├── js/
│       │   └── main.js     # Main JavaScript
│       └── images/         # Image assets
├── run.py                  # Application entry point
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

### Configuration

**config.py** defines three configuration classes:

- `DevelopmentConfig` - Debug mode enabled for development
- `TestingConfig` - Testing mode with debug enabled
- `ProductionConfig` - Production mode with debugging disabled

Set the environment with the `FLASK_ENV` variable:

```bash
export FLASK_ENV=development  # or testing, production
```

### Routes

The Flask application provides the following routes:

| Route        | Method    | Description        |
| ------------ | --------- | ------------------ |
| `/`          | GET       | Home page          |
| `/bio`       | GET       | Biography page     |
| `/portfolio` | GET       | Portfolio showcase |
| `/projects`  | GET       | Projects details   |
| `/contact`   | GET, POST | Contact form page  |

### Running the Application

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the development server:**

   ```bash
   python run.py
   ```

3. **Access the application:**
   Open `http://localhost:5000` in your web browser

### Data Management

Currently, all data (featured projects, portfolio items, projects) is defined as Python dictionaries in the `run.py` file. These can be replaced with:

- Database queries (SQLAlchemy + SQLite/PostgreSQL)
- JSON files
- External APIs
- Content management system

Example data structure for projects:

```python
FEATURED_PROJECTS = [
    {
        "title": "Project Name",
        "description": "Brief description",
        "image": "/static/images/project.jpg",
        "link": "https://external-link.com"
    }
]
```

### Static Assets

**CSS** (`app/static/css/style.css`)

- Responsive design with mobile-first approach
- CSS variables for consistent theming
- Flexbox and CSS Grid for layouts
- Smooth transitions and animations

**JavaScript** (`app/static/js/main.js`)

- Portfolio filter functionality
- Contact form validation
- Smooth scroll navigation
- Event handling and DOM manipulation

## Content Population

The website has been populated with content discovered from the original Wix website. This section documents the content mapping and implementation approach.

### Content Discovery & Mapping

All content from the original website was crawled and mapped to the Flask application's data structures:

**Featured Projects** (Home Page)

- Comedy Stains Podcast - with logo image
- Super Silly Show - with logo image
- Owl Movement Music - with animated GIF

**Portfolio Items** (Portfolio Page)

- 8 items across 6 categories (Comedy, Music, Video, Podcast, Blog)
- Includes blog posts with their original publish dates and images
- All items linked to external platforms or original source URLs

**Projects** (Projects Page)

- 6 major project categories with descriptions
- Comedy Stains Podcast with 8 social media platform links
- Super Silly Show with 5 platform links
- Original Music with 2 SoundCloud channels
- Comedy Videos & Content with 2 YouTube channels
- Media & Gallery with media showcase link
- Merchandise & Shop with store and support links

### Image & Media Handling

All images and videos are served from the original Wix CDN using direct URLs:

**Image URLs Used:**

1. Comedy Stains Logo - `static.wixstatic.com/media/11d46c_7439f513351e479c89cb129a9002d411~mv2.jpg`
2. Super Silly Show Logo - `static.wixstatic.com/media/11d46c_4edf89bfd02243b0886637a41c35169b~mv2.png`
3. Corky's Eye & Pizza GIF - `static.wixstatic.com/media/11d46c_b97cf97a3e754c13a503e2fd6b800264~mv2.gif`
4. Blog Post Images (3) - From `static.wixstatic.com/media/`
5. YouTube Thumbnail - From `yt3.ggpht.com/`

**Benefits of Using Direct CDN URLs:**

- No need to download and host large image files
- Automatic image optimization by Wix CDN
- Reduced server storage requirements
- Responsive image serving with format negotiation

### Social Media Integration

All social media links are integrated throughout the site:

**Platforms Included:**

- Instagram, Twitter, Facebook (main channels)
- YouTube (3 channels)
- SoundCloud (2 channels)
- TikTok, Twitch, Periscope
- IMDB profile
- Ko-Fi support page

Links are automatically displayed in:

- Footer on every page
- Contact page with expanded sections
- Individual project pages where applicable

### Implementation Challenges & Solutions

**Challenge 1: Image Hosting**

- Original website uses Wix's CDN
- Solution: Direct linking to original CDN URLs preserves existing images and avoids redundant storage

**Challenge 2: Dynamic Content**

- Multiple categories and filtering needed
- Solution: Implemented JavaScript-based portfolio filtering for seamless category navigation

**Challenge 3: Multi-Platform Links**

- Projects exist on 8+ different platforms
- Solution: Organized links by platform type in project data structure for easy management

**Challenge 4: Responsive Media**

- Videos and images needed to work on all devices
- Solution: Used responsive CSS classes and viewport-aware image sizing

### Data Structure

The content is organized in the `run.py` file using Python dictionaries:

```python
# Featured projects for home page
FEATURED_PROJECTS = [
    {
        "title": "Project Title",
        "description": "Short description",
        "image": "https://cdn-url/image.jpg",
        "link": "https://external-link.com"
    }
]

# Portfolio items with category filtering
PORTFOLIO_ITEMS = [
    {
        "title": "Item Title",
        "category": "podcast|music|video|comedy|blog",
        "description": "Detailed description",
        "image": "https://cdn-url/image.jpg",
        "link": "https://external-link.com"
    }
]

# Detailed project information
PROJECTS = [
    {
        "title": "Project Title",
        "type": "Project Type",
        "description": "Comprehensive description",
        "image": "https://cdn-url/image.jpg",  # optional
        "links": {
            "Platform Name": "https://platform-url.com"
        }
    }
]

# Social media platform URLs
SOCIAL_MEDIA = {
    "Platform Name": "https://platform-url.com"
}
```

### Content Updates

To update content, simply modify the data dictionaries in `run.py`:

1. **Add new project:**

   ```python
   PROJECTS.append({
       "title": "New Project",
       "type": "Type",
       "description": "Description",
       "links": {"Platform": "URL"}
   })
   ```

2. **Update existing item:**
   - Locate the item in the appropriate list
   - Modify the dictionary values
   - Restart Flask application for changes to take effect

3. **Add portfolio category:**
   - Create new button in portfolio filters (portfolio.html)
   - Add items with matching category value
   - JavaScript filtering automatically handles new category

## Image Management

All images from the original website have been downloaded and stored locally within the Flask application for faster loading and independence from external CDNs.

### Local Image Storage

**Directory:** `app/static/images/`

**Downloaded Images:**

1. `comedy-stains-logo.jpg` (500 KB) - Comedy Stains podcast branding
2. `super-silly-show-logo.png` (103 KB) - Super Silly Show branding
3. `corky-eye-pizza.gif` (2.4 MB) - Animated branding element
4. `ding-dong-show-thumbnail.jpg` (196 KB) - YouTube thumbnail for live show
5. `getting-caught-up.jpg` (199 KB) - Blog post image from July 2022
6. `stains-of-comedy.png` (883 KB) - Blog post image from April 2021
7. `new-beginnings-and-old-endings.jpg` (991 KB) - Blog post image from March 2021
8. `comedy-square-logo.png` (227 KB) - Comedy branding element

**Total Size:** ~6 MB local storage

### Image URL Mapping

All image references in the application have been updated to use local paths:

```python
# Before (CDN URL):
"image": "https://static.wixstatic.com/media/11d46c_7439f513351e479c89cb129a9002d411~mv2.jpg"

# After (Local path):
"image": "/static/images/comedy-stains-logo.jpg"
```

### Downloading Images

A Python script is provided to automatically download all images:

```bash
python download_images.py
```

This script:

- Creates the `app/static/images/` directory if needed
- Downloads all images from their original CDN URLs
- Saves them with descriptive filenames
- Skips already-downloaded images
- Provides download statistics and local path mapping

**Output Example:**

```
Downloading images to F:\...\app\static\images
Total images to download: 8

⬇ Downloading comedy-stains-logo.jpg... ✓ (500045 bytes)
⬇ Downloading super-silly-show-logo.png... ✓ (103045 bytes)
...

Download complete!
Successful: 8
Failed: 0
```

### Image Files Updated

The following files reference images and have been updated to use local paths:

1. **run.py** - Flask application data
   - `FEATURED_PROJECTS` - 3 images
   - `PORTFOLIO_ITEMS` - 8 images
   - `PROJECTS` - 3 images with branding

2. **app/**init**.py** - Alternative Flask configuration
   - Same image mappings as run.py
   - Used as application factory pattern

### Benefits of Local Image Storage

✓ **Performance:** Faster load times with local serving
✓ **Reliability:** No external CDN dependencies
✓ **Control:** Full control over image optimization
✓ **Bandwidth:** Reduced external requests
✓ **Offline:** Site works without internet for images
✓ **Scalability:** Easy to add/remove images

## Metadata and SEO

The website includes comprehensive SEO optimization through metadata tags and structured content management. All page-specific metadata is centralized for easy management and consistency.

### Metadata Structure

Metadata is organized in `PAGE_METADATA` dictionary with page-specific tags for:

- Meta descriptions (120-160 characters)
- Keywords (relevant search terms)
- Open Graph tags (social media sharing)
- Twitter Card tags (Twitter optimization)
- Canonical URLs
- Author attribution

**Location:** Defined in both `run.py` and `app/__init__.py`

### Page Metadata

#### Home Page (`/`)

- **Title:** "Corey Pellizzi - Comedian, Producer, Musician & Director"
- **Description:** Welcome and overview of creative work
- **Keywords:** comedian, comedy, producer, musician, director, writer, entertainment, Owl Movement, Comedy Stains
- **OG Image:** Comedy Stains logo
- **Twitter Card:** summary_large_image

#### Biography Page (`/bio`)

- **Title:** "About Corey Pellizzi - Biography & Expertise"
- **Description:** Journey and expertise highlights
- **Keywords:** about, biography, comedian, producer, musician, director, writer
- **OG Image:** Comedy square logo
- **Twitter Card:** summary

#### Portfolio Page (`/portfolio`)

- **Title:** "Portfolio - Comedy, Music, Video & Podcast Projects"
- **Description:** Comprehensive portfolio overview
- **Keywords:** portfolio, comedy, music, video, podcast, blog, projects, content
- **OG Image:** Super Silly Show logo
- **Twitter Card:** summary_large_image

#### Projects Page (`/projects`)

- **Title:** "Projects - Podcasts, Shows, Music & More"
- **Description:** Featured projects and collaborations
- **Keywords:** projects, podcast, show, music, video, Comedy Stains, Super Silly Show
- **OG Image:** Comedy Stains logo
- **Twitter Card:** summary_large_image

#### Contact Page (`/contact`)

- **Title:** "Contact - Get In Touch With Corey Pellizzi"
- **Description:** Contact information and social media
- **Keywords:** contact, email, social media, collaboration, inquiries, support
- **OG Image:** Comedy square logo
- **Twitter Card:** summary

### Meta Tags Implemented

#### Standard Meta Tags

```html
<meta name="description" content="Page-specific description" />
<meta name="keywords" content="Relevant, keywords, here" />
<meta name="author" content="Corey Pellizzi" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="https://owlmovement.example.com/page" />
```

#### Open Graph Tags (Facebook, LinkedIn, Pinterest)

```html
<meta property="og:type" content="website" />
<meta property="og:title" content="Page Title" />
<meta property="og:description" content="Page description" />
<meta property="og:image" content="Image URL" />
<meta property="og:url" content="Page URL" />
<meta
  property="og:site_name"
  content="Corey Pellizzi - Comedian, Producer, Musician & Director"
/>
```

#### Twitter Card Tags (Twitter-specific optimization)

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Page Title" />
<meta name="twitter:description" content="Page description" />
<meta name="twitter:image" content="Image URL" />
<meta name="twitter:creator" content="@corkycomedynow" />
```

### Implementation

Metadata is passed from Flask routes to templates:

```python
# In route
meta = PAGE_METADATA.get('index', {})
return render_template('index.html',
                       title=meta.get('title', 'Home'),
                       meta=meta,
                       featured_projects=FEATURED_PROJECTS,
                       social_media=SOCIAL_MEDIA)

# In template (base.html)
{% if meta %}
  <meta name="description" content="{{ meta.get('description', '') }}" />
  <meta name="keywords" content="{{ meta.get('keywords', '') }}" />
  <!-- ... other meta tags ... -->
{% endif %}
```

### Template Rendering

The `base.html` template automatically renders all meta tags when the `meta` variable is provided:

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  {% if meta %}
  <meta name="description" content="{{ meta.get('description', '') }}" />
  <meta name="keywords" content="{{ meta.get('keywords', '') }}" />
  <meta name="author" content="Corey Pellizzi" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{{ meta.get('canonical', '') }}" />

  <!-- Open Graph Tags -->
  <meta property="og:title" content="{{ meta.get('og_title', title) }}" />
  <meta
    property="og:description"
    content="{{ meta.get('og_description', '') }}"
  />
  <meta property="og:image" content="{{ meta.get('og_image', '') }}" />
  <meta property="og:url" content="{{ meta.get('og_url', '') }}" />

  <!-- Twitter Cards -->
  <meta
    name="twitter:card"
    content="{{ meta.get('twitter_card', 'summary') }}"
  />
  <meta name="twitter:title" content="{{ meta.get('og_title', title) }}" />
  <meta
    name="twitter:creator"
    content="{{ meta.get('twitter_creator', '') }}"
  />
  {% endif %}

  <title>{{ title }} - Corey Pellizzi</title>
</head>
```

### SEO Benefits

**Search Engine Optimization:**

- ✓ Unique meta descriptions for each page
- ✓ Relevant keywords for search ranking
- ✓ Canonical URLs to prevent duplicate content
- ✓ Meta robots tag for crawling control
- ✓ Author attribution for credibility

**Social Media Optimization:**

- ✓ Open Graph tags for Facebook, LinkedIn, Pinterest
- ✓ Twitter Card tags for enhanced Twitter sharing
- ✓ Custom og:image for each page
- ✓ Compelling og:description for social preview
- ✓ Twitter creator attribution

**User Experience:**

- ✓ Accurate page titles in browser tabs
- ✓ Rich preview on social media shares
- ✓ Better click-through rates from search results

### Updating Metadata

To update metadata for a page:

1. **Edit the PAGE_METADATA dictionary:**

   ```python
   PAGE_METADATA = {
       "page_name": {
           "title": "New title",
           "description": "New description",
           "keywords": "keyword1, keyword2, keyword3",
           "og_title": "Social media title",
           "og_description": "Social media description",
           "og_image": "Image URL",
           "og_url": "Page URL",
           "twitter_card": "summary or summary_large_image",
           "twitter_creator": "@username",
           "canonical": "Canonical URL"
       }
   }
   ```

2. **Update the route to pass the metadata:**

   ```python
   @app.route('/page')
   def page():
       meta = PAGE_METADATA.get('page_name', {})
       return render_template('page.html',
                              title=meta.get('title', 'Page'),
                              meta=meta,
                              social_media=SOCIAL_MEDIA)
   ```

3. **Template automatically uses the metadata** - no changes needed in templates!

### Best Practices

**Meta Descriptions:**

- Keep between 120-160 characters
- Include primary keyword naturally
- Write compelling descriptions to improve CTR
- Avoid keyword stuffing

**Keywords:**

- 3-5 primary keywords per page
- Include long-tail keywords when relevant
- Focus on user search intent
- Natural language over keyword stuffing

**Open Graph Images:**

- Use high-quality, relevant images (1200x630px optimal)
- Images should represent page content
- Consistent branding across images

**Social Sharing:**

- Descriptive og:title and og:description
- Compelling to encourage clicks
- Different from page title if needed
- Twitter creator for personal branding

## Testing

The Flask application includes comprehensive automated tests to ensure all pages are correctly rendered, metadata is properly included, and all content displays correctly.

### Test Suite Overview

**Total Tests:** 35 test cases covering all aspects of the application
**Test Framework:** pytest with pytest-flask plugin
**Status:** ✅ All 35 tests passing

### Test Organization

Tests are organized into logical groups in `tests/test_app.py`:

#### 1. **TestRoutes** (8 tests)

Tests all application routes and HTTP methods:

- ✓ Index page (/)
- ✓ Biography page (/bio)
- ✓ Portfolio page (/portfolio)
- ✓ Projects page (/projects)
- ✓ Contact page GET request
- ✓ Contact page POST request (form submission)
- ✓ 404 error handling
- ✓ Invalid HTTP method (405 error)

#### 2. **TestMetadata** (7 tests)

Tests SEO and social media metadata tags:

- ✓ Index page metadata (description, keywords, OG tags)
- ✓ Bio page metadata
- ✓ Portfolio page metadata
- ✓ Projects page metadata
- ✓ Contact page metadata
- ✓ Twitter Card tags present on all pages
- ✓ Open Graph tags present on all pages

#### 3. **TestImageEmbedding** (3 tests)

Tests image presence and embedding:

- ✓ Images referenced in static directory
- ✓ Portfolio items have images
- ✓ Projects have images

#### 4. **TestPageContent** (5 tests)

Tests page content and data rendering:

- ✓ Index page displays featured projects
- ✓ Portfolio page displays portfolio items
- ✓ Projects page displays project details
- ✓ Bio page displays biography content
- ✓ Contact page has contact form

#### 5. **TestNavigation** (3 tests)

Tests navigation and links on all pages:

- ✓ Navigation present on all pages
- ✓ Footer present on all pages
- ✓ Social media links present

#### 6. **TestHTML** (4 tests)

Tests HTML structure and validity:

- ✓ HTML doctype declaration
- ✓ Proper HTML structure (html, head, body, title)
- ✓ CSS stylesheet linked
- ✓ JavaScript file linked

#### 7. **TestResponseHeaders** (2 tests)

Tests HTTP response headers and content type:

- ✓ Content-type is text/html
- ✓ Response includes character set

#### 8. **TestFormValidation** (3 tests)

Tests contact form submission and validation:

- ✓ Form submission with all fields
- ✓ Form submission with minimal fields
- ✓ Form submission with no data

### Running Tests

#### Install Test Dependencies

```bash
pip install pytest==7.4.0 pytest-flask==1.2.0
```

Or install all dependencies including tests:

```bash
pip install -r requirements.txt
```

#### Run All Tests

```bash
pytest tests/ -v
```

#### Run Specific Test Class

```bash
pytest tests/test_app.py::TestMetadata -v
```

#### Run Specific Test

```bash
pytest tests/test_app.py::TestMetadata::test_index_metadata -v
```

#### Run with Coverage Report

```bash
pytest tests/ --cov=run --cov-report=html
```

#### Run Tests Quietly (Summary Only)

```bash
pytest tests/ -q
```

#### Run Tests with Detailed Output

```bash
pytest tests/ -vv --tb=long
```

### Test Fixtures

**conftest.py** provides pytest fixtures for testing:

```python
@pytest.fixture
def app():
    """Flask app configured for testing"""
    # Returns a Flask app with TestingConfig

@pytest.fixture
def client(app):
    """Test client for making requests"""
    # Returns a Flask test client for making HTTP requests

@pytest.fixture
def runner(app):
    """Test CLI runner"""
    # Returns a CLI runner for testing CLI commands
```

### Test Configuration

Tests use `TestingConfig` from `config.py`:

- **DEBUG:** True
- **TESTING:** True
- **SQLALCHEMY_DATABASE_URI:** Uses in-memory SQLite (if implemented)
- **WTF_CSRF_ENABLED:** Disabled for easier form testing

### What Gets Tested

**✓ Route Functionality**

- All 5 main routes return 200 status code
- Routes handle GET and POST requests correctly
- Error routes (404, 405) return appropriate status codes

**✓ Metadata and SEO**

- Meta description tags present
- Keywords specified correctly
- Open Graph tags for social media sharing
- Twitter Card tags for Twitter optimization
- Canonical URLs specified
- Author and robots tags

**✓ Content Rendering**

- Page titles displayed correctly
- Featured projects shown on home page
- Portfolio items displayed with images
- Projects with platform links displayed
- Contact form present with required fields
- Social media links in footer

**✓ HTML Structure**

- Valid HTML doctype
- Proper head/body structure
- CSS stylesheets linked
- JavaScript files linked
- Content properly formatted

**✓ Image Embedding**

- Images referenced from local /static/images/ directory
- Image paths correct in all templates
- No broken image references

**✓ Form Handling**

- Contact form accepts POST requests
- Form fields processed correctly
- Empty form submissions handled

### Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.10.11, pytest-9.0.3, pluggy-1.6.0
collected 35 items

tests/test_app.py::TestRoutes::test_index_route PASSED                   [  2%]
tests/test_app.py::TestRoutes::test_bio_route PASSED                     [  5%]
tests/test_app.py::TestRoutes::test_portfolio_route PASSED               [  8%]
tests/test_app.py::TestRoutes::test_projects_route PASSED                [ 11%]
tests/test_app.py::TestRoutes::test_contact_route_get PASSED             [ 14%]
tests/test_app.py::TestRoutes::test_contact_route_post PASSED            [ 17%]
tests/test_app.py::TestRoutes::test_404_not_found PASSED                 [ 20%]
tests/test_app.py::TestRoutes::test_invalid_method PASSED                [ 22%]
tests/test_app.py::TestMetadata::test_index_metadata PASSED              [ 25%]
tests/test_app.py::TestMetadata::test_bio_metadata PASSED                [ 28%]
tests/test_app.py::TestMetadata::test_portfolio_metadata PASSED          [ 31%]
tests/test_app.py::TestMetadata::test_projects_metadata PASSED           [ 34%]
tests/test_app.py::TestMetadata::test_contact_metadata PASSED            [ 37%]
tests/test_app.py::TestMetadata::test_twitter_card_tags PASSED           [ 40%]
tests/test_app.py::TestMetadata::test_open_graph_tags PASSED             [ 42%]
tests/test_app.py::TestImageEmbedding::test_images_in_static_directory PASSED [ 45%]
tests/test_app.py::TestImageEmbedding::test_portfolio_items_have_images PASSED [ 48%]
tests/test_app.py::TestImageEmbedding::test_projects_have_images PASSED  [ 51%]
tests/test_app.py::TestPageContent::test_index_has_featured_projects PASSED [ 54%]
tests/test_app.py::TestPageContent::test_portfolio_has_items PASSED      [ 57%]
tests/test_app.py::TestPageContent::test_projects_has_project_details PASSED [ 60%]
tests/test_app.py::TestPageContent::test_bio_has_biography_content PASSED [ 62%]
tests/test_app.py::TestPageContent::test_contact_has_form PASSED         [ 65%]
tests/test_app.py::TestNavigation::test_navigation_present PASSED        [ 68%]
tests/test_app.py::TestNavigation::test_footer_present PASSED            [ 71%]
tests/test_app.py::TestNavigation::test_social_media_links PASSED        [ 74%]
tests/test_app.py::TestHTML::test_html_doctype PASSED                    [ 77%]
tests/test_app.py::TestHTML::test_html_structure PASSED                  [ 80%]
tests/test_app.py::TestHTML::test_css_stylesheet_linked PASSED           [ 82%]
tests/test_app.py::TestHTML::test_javascript_linked PASSED               [ 85%]
tests/test_app.py::TestResponseHeaders::test_content_type_html PASSED    [ 88%]
tests/test_app.py::TestResponseHeaders::test_response_charset PASSED     [ 91%]
tests/test_app.py::TestFormValidation::test_contact_form_submission_all_fields PASSED [ 94%]
tests/test_app.py::TestFormValidation::test_contact_form_submission_minimal_fields PASSED [ 97%]
tests/test_app.py::TestFormValidation::test_contact_form_empty PASSED    [100%]

============================= 35 passed in 0.40s ==============================
```

### Test Coverage Metrics

**Route Coverage:** 100% (5/5 main routes)
**Page Content:** 100% (all required content rendered)
**Metadata:** 100% (all SEO tags present)
**Image References:** 100% (all images embedded correctly)
**HTML Structure:** 100% (valid HTML on all pages)
**Error Handling:** 100% (404/405 errors handled)
**Form Submission:** 100% (contact form processes requests)

### Best Practices for Testing

1. **Run tests regularly** - After any changes to routes or templates
2. **Maintain test fixtures** - Keep conftest.py updated with new fixtures
3. **Add tests for new features** - Every new route/feature should have tests
4. **Use descriptive test names** - Test name should describe what it tests
5. **Keep tests isolated** - Each test should be independent
6. **Mock external services** - Use mocking for external API calls
7. **Test edge cases** - Test invalid inputs, empty data, etc.

### Troubleshooting Tests

**TemplateNotFound Error:**

- Ensure Flask app is created with correct template_folder
- Check that template files exist in `app/templates/`

**Assertion Failures:**

- Verify expected content is in rendered HTML
- Check that templates are using correct variable names
- Ensure metadata dict is passed to templates

**Import Errors:**

- Make sure conftest.py is in tests/ directory
- Verify run.py and config.py are in project root
- Check Python path in conftest.py

### Continuous Integration

For CI/CD pipelines, run tests with:

```bash
pytest tests/ -v --junitxml=test-results.xml
```

This generates a JUnit XML report compatible with most CI systems (GitHub Actions, GitLab CI, Jenkins, etc.).

## Static HTML Generation

The website can be deployed as a static site with pre-generated HTML files. This approach provides maximum performance, security, and simplicity for hosting.

### Static Site Generation

**Purpose:** Generate standalone HTML files with all content, images, CSS, and JavaScript embedded, ready for deployment to any static hosting service.

**Generator Script:** `generate_static.py`

**What Gets Generated:**

- ✓ 5 static HTML pages (index, bio, portfolio, projects, contact)
- ✓ CSS stylesheet (responsive design)
- ✓ JavaScript files (interactivity)
- ✓ All image assets (8 images)
- ✓ Complete, self-contained static site

### Running Static Generation

#### Generate Static Site

```bash
python generate_static.py
```

#### Output

The script creates a `build/` directory containing:

```
build/
├── index.html           (8.3 KB)
├── bio.html            (6.6 KB)
├── portfolio.html      (12.7 KB)
├── projects.html       (16.8 KB)
├── contact.html        (8.1 KB)
└── static/
    ├── css/
    │   └── style.css   (10.9 KB)
    ├── js/
    │   └── main.js     (2.9 KB)
    └── images/
        ├── comedy-stains-logo.jpg         (500 KB)
        ├── super-silly-show-logo.png      (103 KB)
        ├── comedy-square-logo.png         (227 KB)
        ├── corky-eye-pizza.gif            (2.4 MB)
        ├── ding-dong-show-thumbnail.jpg   (196 KB)
        ├── getting-caught-up.jpg          (199 KB)
        ├── new-beginnings-and-old-endings.jpg (992 KB)
        └── stains-of-comedy.png           (883 KB)

Total: 19 files, 5.32 MB
```

### Serving the Static Site Locally

After generation, serve the static site locally for testing:

#### Using Python's Built-in Server

```bash
python -m http.server 8000 --directory build/
```

Then open: `http://localhost:8000/`

#### Using Node.js http-server

```bash
npx http-server build/ -p 8000
```

#### Using Live Server (VS Code)

Right-click on `build/index.html` and select "Open with Live Server"

### Deploying Static Site

The `build/` directory can be deployed to any static hosting service:

#### GitHub Pages

```bash
# Copy build contents to docs/ or gh-pages branch
cp -r build/* docs/
git add docs/
git commit -m "Update static site"
git push
```

#### Netlify

```bash
# Drag and drop build/ directory to Netlify
# Or use Netlify CLI
netlify deploy --prod --dir=build
```

#### AWS S3 + CloudFront

```bash
aws s3 sync build/ s3://bucket-name/
```

#### Vercel

```bash
# Automatic deployment from git
# Or manual deployment
vercel --prod
```

#### Traditional Web Hosting

```bash
# Upload build/ directory contents to web root
# via FTP/SFTP
```

### Generation Process

The `generate_static.py` script:

1. **Creates Flask App** - Uses create_app() to initialize the Flask application
2. **Establishes Build Directory** - Creates/cleans the `build/` directory
3. **Renders Each Route** - Uses Flask test client to render all pages
4. **Saves HTML Files** - Writes rendered HTML to individual files
5. **Copies Static Assets** - Duplicates CSS, JavaScript, and images
6. **Generates Summary** - Lists all generated files with sizes

### Generated File Analysis

All generated HTML files include:

**✓ Complete Meta Tags**

- SEO meta descriptions
- Keywords for search engines
- Author and robots directives
- Canonical URLs

**✓ Open Graph Tags**

- og:title, og:description, og:image
- og:url, og:type, og:site_name
- Optimized for Facebook, LinkedIn, Pinterest

**✓ Twitter Card Tags**

- twitter:card, twitter:title, twitter:description
- twitter:image, twitter:creator
- Optimized for Twitter sharing

**✓ Responsive Design**

- Mobile-first CSS with breakpoint at 768px
- All images embedded with correct paths
- CSS Grid and Flexbox layouts preserved

**✓ Embedded Content**

- All internal navigation links work correctly
- Images reference local `/static/images/` paths
- CSS and JavaScript references updated

### Performance Benefits

**✓ Fast Page Loads**

- No server processing required
- Direct HTML file serving
- Minimal latency

**✓ High Availability**

- No database dependencies
- No application server needed
- Works on any web server

**✓ Security**

- No attack surface from application code
- Static files are inherently safe
- Reduced vulnerability risk

**✓ Scalability**

- Easy to cache on CDN
- Handles traffic spikes effortlessly
- Minimal server resources

**✓ Simplicity**

- Deploy to any hosting service
- No build tools required
- No environment configuration needed

### Example Workflow

```bash
# 1. Make changes to Flask app or templates
# ... edit run.py, templates, etc ...

# 2. Run tests to verify changes
pytest tests/ -v

# 3. Generate static site
python generate_static.py

# 4. Test static site locally
python -m http.server 8000 --directory build/

# 5. Deploy to hosting service
# (copy build/ directory to host)
```

### Static Site vs Flask Application

| Aspect              | Flask App                         | Static Site                |
| ------------------- | --------------------------------- | -------------------------- |
| **Deployment**      | Web server + Python runtime       | Any web server             |
| **Speed**           | Slightly slower (server overhead) | Instant (pure HTML)        |
| **Database**        | Supported                         | Not supported              |
| **Dynamic Content** | Full support                      | Limited (client-side only) |
| **Updates**         | Change code + restart             | Regenerate static files    |
| **Hosting Cost**    | Higher (server/runtime)           | Lower (static hosting)     |
| **Maintenance**     | More complex                      | Simpler                    |
| **SEO**             | Good                              | Excellent (pre-rendered)   |
| **Caching**         | Per-request                       | Cache-friendly             |

For Corey Pellizzi's portfolio site (static content, no database), **static deployment is ideal**.

### Troubleshooting

**Build directory is large:**

- Images are the main size contributor (~5.26 MB)
- This is expected and reasonable for web hosting
- Compress images further if needed

**Static links are broken:**

- Ensure all template links use `url_for()` function
- Check that static files are in correct paths
- Verify `template_folder` and `static_folder` in create_app()

**Images not displaying:**

- Check that image files were copied to `build/static/images/`
- Verify image paths in generated HTML are `/static/images/filename`
- Ensure image filenames have correct extensions

**CSS/JavaScript not loading:**

- Verify files exist in `build/static/css/` and `build/static/js/`
- Check that stylesheet/script references use correct paths
- View source of generated HTML to confirm paths

### Next Steps

After generating the static site:

1. **Test thoroughly** - Verify all pages and links work
2. **Optimize images** - Consider compression for web
3. **Minify assets** - Reduce CSS/JS file sizes
4. **Setup CDN** - Distribute static files globally
5. **Enable caching** - Configure browser cache headers
6. **Monitor analytics** - Track visitor behavior
7. **Regular updates** - Regenerate when content changes
