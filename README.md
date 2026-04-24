# Owlmovement website

This is the repository for the Owlmovement website.

## Content

see [docs/content.md](docs/content.md) for a comprehensive documentation of all discovered content from the original website crawl, including page-specific content details and media assets.

## Flask Application

The website is built using **Flask**, a lightweight Python web framework. The application serves dynamic content and handles routing.

### Project Structure

```text
owlmovement/
├── app/
│   ├── templates/          # Jinja2 HTML templates
│   │   ├── _base.html       # Base template
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

All dynamic content (projects, portfolio items, social links) is stored in **content.json** for easy management without modifying code. Page metadata (SEO tags) is stored separately in **metadata.json**. The Flask application loads both JSON files at startup.

#### content.json Structure

The `content.json` file contains five main sections:

##### 1. **featured_projects**

Projects highlighted on the home and projects pages. Each project includes:

```json
{
  "title": "Project Name",
  "description": "Brief description of the project",
  "image": "/static/images/project-image.jpg",
  "link": "https://external-link.com"
}
```

##### 2. **portfolio_items**

Portfolio gallery items with multi-category support. Each item includes:

```json
{
  "title": "Portfolio Item Name",
  "categories": ["music", "video"],
  "description": "Item description",
  "image": "/static/images/portfolio-image.jpg",
  "link": "https://external-link.com"
}
```

**Available categories:** `comedy`, `music`, `video`, `podcast`

##### 3. **projects**

Detailed project pages with multiple links. Each project includes:

```json
{
  "title": "Project Name",
  "type": "Project Type (e.g., Podcast, Show, Music Production)",
  "description": "Detailed project description",
  "image": "/static/images/project-image.jpg",
  "links": {
    "Link Label": "https://external-link.com",
    "Another Link": "https://another-link.com"
  }
}
```

##### 4. **social_media**

Social media links displayed in footer and contact page:

````json
{
##### 5. **social_media**

Social media links displayed in footer and contact page:

```json
{
  "platform_name": "https://platform-url.com/profile"
}
````

#### metadata.json Structure

Page metadata (SEO tags) for each route is stored in a separate **metadata.json** file. This keeps content and metadata organized for better SEO management.

The `metadata.json` file contains an entry for each page with the following structure:

```json
{
  "page_name": {
    "title": "Page Title",
    "description": "Page description for meta tags",
    "keywords": "keyword1, keyword2, keyword3",
    "og_title": "OpenGraph title",
    "og_description": "OpenGraph description",
    "og_image": "https://image-url.com/image.jpg",
    "og_url": "https://page-url.com",
    "twitter_card": "summary_large_image",
    "twitter_creator": "@twitter_handle",
    "canonical": "https://canonical-url.com"
  }
}
```

**Page names:** `index`, `bio`, `portfolio`, `projects`, `contact`

#### Editing content.json and metadata.json

To add or update content:

1. For content (projects, portfolio, social links): Open `content.json` in your text editor
2. For metadata (SEO tags): Open `metadata.json` in your text editor
3. Locate the relevant section and add or modify entries following the structures documented above
4. Restart the Flask application for changes to take effect
5. Run `python generate_static.py` to update the static site

**Note:** Ensure the JSON files are valid by checking syntax (balanced braces, proper quotes, commas)

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

## Templating

The website uses **Jinja2 templates** to create dynamic HTML pages. The templating system is organized hierarchically with a base template that all pages inherit from.

### Template Structure

**Base Template** (`app/templates/_base.html`)

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
2. Start with: `{% extends "_base.html" %}`
3. Define content block: `{% block content %} ... {% endblock %}`
4. Create a Flask route to render the template
5. Pass required variables from the route

Example:

```jinja2
{% extends "_base.html" %}

{% block content %}
<section class="page-section">
    <div class="container">
        <h1>{{ page_title }}</h1>
        <!-- Your content here -->
    </div>
</section>
{% endblock %}
```

## Metadata and SEO

The website includes comprehensive SEO optimization through metadata tags and structured content management. All page-specific metadata is centralized for easy management and consistency. For detailed documentation on the metadata structure and SEO implementation, see [docs/metadata.md](docs/metadata.md).

## Testing

The application is tested using **pytest** and **pytest-flask** to ensure that all pages are correctly rendered, and that all images and videos are properly embedded and displayed on the pages. For detailed documentation on the testing process and test cases, see [docs/testing.md](docs/testing.md).

## Static HTML Generation

The website can be deployed as a static site with pre-generated HTML files. This approach provides maximum performance, security, and simplicity for hosting. For detailed documentation on the static site generation process and analysis of the generated files, see [docs/static_site.md](docs/static_site.md).
