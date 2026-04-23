# Metadata and SEO

The website includes comprehensive SEO optimization through metadata tags and structured content management. All page-specific metadata is centralized for easy management and consistency.

## Metadata Structure

Metadata is organized in `PAGE_METADATA` dictionary with page-specific tags for:

- Meta descriptions (120-160 characters)
- Keywords (relevant search terms)
- Open Graph tags (social media sharing)
- Twitter Card tags (Twitter optimization)
- Canonical URLs
- Author attribution

**Location:** Defined in both `run.py` and `app/__init__.py`

## Page Metadata

### Home Page (`/`)

- **Title:** "Corey Pellizzi - Comedian, Producer, Musician & Director"
- **Description:** Welcome and overview of creative work
- **Keywords:** comedian, comedy, producer, musician, director, writer, entertainment, Owl Movement, Comedy Stains
- **OG Image:** Comedy Stains logo
- **Twitter Card:** summary_large_image

### Biography Page (`/bio`)

- **Title:** "About Corey Pellizzi - Biography & Expertise"
- **Description:** Journey and expertise highlights
- **Keywords:** about, biography, comedian, producer, musician, director, writer
- **OG Image:** Comedy square logo
- **Twitter Card:** summary

### Portfolio Page (`/portfolio`)

- **Title:** "Portfolio - Comedy, Music, Video & Podcast Projects"
- **Description:** Comprehensive portfolio overview
- **Keywords:** portfolio, comedy, music, video, podcast, blog, projects, content
- **OG Image:** Super Silly Show logo
- **Twitter Card:** summary_large_image

### Projects Page (`/projects`)

- **Title:** "Projects - Podcasts, Shows, Music & More"
- **Description:** Featured projects and collaborations
- **Keywords:** projects, podcast, show, music, video, Comedy Stains, Super Silly Show
- **OG Image:** Comedy Stains logo
- **Twitter Card:** summary_large_image

### Contact Page (`/contact`)

- **Title:** "Contact - Get In Touch With Corey Pellizzi"
- **Description:** Contact information and social media
- **Keywords:** contact, email, social media, collaboration, inquiries, support
- **OG Image:** Comedy square logo
- **Twitter Card:** summary

## Meta Tags Implemented

### Standard Meta Tags

```html
<meta name="description" content="Page-specific description" />
<meta name="keywords" content="Relevant, keywords, here" />
<meta name="author" content="Corey Pellizzi" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="https://owlmovement.example.com/page" />
```

### Open Graph Tags (Facebook, LinkedIn, Pinterest)

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

### Twitter Card Tags (Twitter-specific optimization)

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Page Title" />
<meta name="twitter:description" content="Page description" />
<meta name="twitter:image" content="Image URL" />
<meta name="twitter:creator" content="@corkycomedynow" />
```

## Implementation

Metadata is passed from Flask routes to templates:

```python
# In route
meta = PAGE_METADATA.get('index', {})
return render_template('index.html',
                       title=meta.get('title', 'Home'),
                       meta=meta,
                       featured_projects=FEATURED_PROJECTS,
                       social_media=SOCIAL_MEDIA)

# In template (_base.html)
{% if meta %}
  <meta name="description" content="{{ meta.get('description', '') }}" />
  <meta name="keywords" content="{{ meta.get('keywords', '') }}" />
  <!-- ... other meta tags ... -->
{% endif %}
```

## Template Rendering

The `_base.html` template automatically renders all meta tags when the `meta` variable is provided:

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

## SEO Benefits

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

## Updating Metadata

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

## Best Practices

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
