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
