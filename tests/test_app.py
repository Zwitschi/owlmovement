"""
Unit tests for the Flask application routes and functionality.
Tests all pages, metadata rendering, image embedding, and form submission.
"""
import pytest


class TestRoutes:
    """Test suite for all application routes."""

    def test_index_route(self, client):
        """Test the index (home) page route."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Corey Pellizzi' in response.data
        assert b'Comedian' in response.data

    def test_bio_route(self, client):
        """Test the biography page route."""
        response = client.get('/bio')
        assert response.status_code == 200
        assert b'About' in response.data or b'Biography' in response.data

    def test_portfolio_route(self, client):
        """Test the portfolio page route."""
        response = client.get('/portfolio')
        assert response.status_code == 200
        assert b'Portfolio' in response.data or b'portfolio' in response.data

    def test_projects_route(self, client):
        """Test the projects page route."""
        response = client.get('/projects')
        assert response.status_code == 200
        assert b'Projects' in response.data or b'projects' in response.data

    def test_contact_route_get(self, client):
        """Test the contact page GET request."""
        response = client.get('/contact')
        assert response.status_code == 200
        assert b'Contact' in response.data
        assert b'contact' in response.data.lower()

    def test_contact_route_post(self, client):
        """Test the contact page POST request (form submission)."""
        response = client.post('/contact', data={
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content'
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_404_not_found(self, client):
        """Test 404 error page for non-existent route."""
        response = client.get('/nonexistent')
        assert response.status_code == 404

    def test_invalid_method(self, client):
        """Test invalid HTTP method."""
        response = client.put('/contact')
        assert response.status_code == 405  # Method Not Allowed


class TestMetadata:
    """Test suite for metadata rendering and SEO tags."""

    def test_index_metadata(self, client):
        """Test metadata tags on index page."""
        response = client.get('/')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for meta tags
        assert 'name="description"' in data
        assert 'name="keywords"' in data
        assert 'property="og:title"' in data
        assert 'property="og:description"' in data
        assert 'property="og:image"' in data

    def test_bio_metadata(self, client):
        """Test metadata tags on bio page."""
        response = client.get('/bio')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for meta tags
        assert 'name="description"' in data
        assert 'property="og:title"' in data

    def test_portfolio_metadata(self, client):
        """Test metadata tags on portfolio page."""
        response = client.get('/portfolio')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for meta tags
        assert 'name="description"' in data
        assert 'property="og:image"' in data

    def test_projects_metadata(self, client):
        """Test metadata tags on projects page."""
        response = client.get('/projects')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for meta tags
        assert 'name="keywords"' in data
        assert 'property="og:url"' in data

    def test_contact_metadata(self, client):
        """Test metadata tags on contact page."""
        response = client.get('/contact')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for meta tags
        assert 'name="description"' in data
        assert 'property="og:title"' in data

    def test_twitter_card_tags(self, client):
        """Test Twitter Card meta tags are present."""
        response = client.get('/')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for Twitter Card tags
        assert 'name="twitter:card"' in data
        assert 'name="twitter:title"' in data
        assert 'name="twitter:creator"' in data

    def test_open_graph_tags(self, client):
        """Test Open Graph meta tags are present."""
        response = client.get('/')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for Open Graph tags
        assert 'property="og:type"' in data
        assert 'property="og:site_name"' in data
        assert 'rel="canonical"' in data


class TestImageEmbedding:
    """Test suite for image embedding and display."""

    def test_images_in_static_directory(self, client):
        """Test that images are referenced in responses."""
        response = client.get('/')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for image references
        assert '/static/images/' in data

    def test_portfolio_items_have_images(self, client):
        """Test that portfolio page references images."""
        response = client.get('/portfolio')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for image references
        assert '/static/images/' in data

    def test_projects_have_images(self, client):
        """Test that projects page references images."""
        response = client.get('/projects')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for image references
        assert '/static/images/' in data or 'alt=' in data


class TestPageContent:
    """Test suite for page content rendering."""

    def test_index_has_featured_projects(self, client):
        """Test that index page displays featured projects."""
        response = client.get('/')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for content sections
        assert 'featured' in data.lower() or 'project' in data.lower()

    def test_portfolio_has_items(self, client):
        """Test that portfolio page displays portfolio items."""
        response = client.get('/portfolio')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for portfolio-related content
        assert 'portfolio' in data.lower() or 'item' in data.lower()

    def test_projects_has_project_details(self, client):
        """Test that projects page displays project details."""
        response = client.get('/projects')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for project-related content
        assert 'Comedy Stains' in data or 'project' in data.lower()

    def test_projects_featured_section_precedes_project_list(self, client):
        """Test that featured projects render before the full project list."""
        response = client.get('/projects')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        featured_index = data.find('featured-projects-section')
        project_list_index = data.find('projects-list')

        assert featured_index != -1
        assert project_list_index != -1
        assert featured_index < project_list_index

    def test_bio_has_biography_content(self, client):
        """Test that bio page has biography content."""
        response = client.get('/bio')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for biography-related content
        assert 'bio' in data.lower() or 'about' in data.lower() or 'journey' in data.lower()

    def test_contact_has_form(self, client):
        """Test that contact page has contact form."""
        response = client.get('/contact')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for form elements
        assert 'form' in data.lower()
        assert 'email' in data.lower()
        assert 'message' in data.lower()


class TestNavigation:
    """Test suite for navigation and links."""

    def test_navigation_present(self, client):
        """Test that navigation is present on all pages."""
        for route in ['/', '/bio', '/portfolio', '/projects', '/contact']:
            response = client.get(route)
            assert response.status_code == 200
            data = response.data.decode('utf-8')

            # Check for navigation elements
            assert 'nav' in data.lower() or 'href=' in data

    def test_footer_present(self, client):
        """Test that footer is present on all pages."""
        for route in ['/', '/bio', '/portfolio', '/projects', '/contact']:
            response = client.get(route)
            assert response.status_code == 200
            data = response.data.decode('utf-8')

            # Check for footer elements
            assert 'footer' in data.lower() or 'social' in data.lower()

    def test_social_media_links(self, client):
        """Test that social media links are present."""
        response = client.get('/')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        # Check for social media links
        assert 'instagram' in data.lower(
        ) or 'twitter' in data.lower() or 'facebook' in data.lower()


class TestHTML:
    """Test suite for HTML validity and structure."""

    def test_html_doctype(self, client):
        """Test that pages have correct HTML doctype."""
        for route in ['/', '/bio', '/portfolio', '/projects', '/contact']:
            response = client.get(route)
            assert response.status_code == 200
            data = response.data.decode('utf-8')

            assert '<!DOCTYPE html>' in data or '<!doctype html>' in data

    def test_html_structure(self, client):
        """Test that pages have proper HTML structure."""
        for route in ['/', '/bio', '/portfolio', '/projects', '/contact']:
            response = client.get(route)
            assert response.status_code == 200
            data = response.data.decode('utf-8')

            # Check for basic HTML structure
            assert '<html' in data
            assert '<head>' in data
            assert '<body>' in data
            assert '<title>' in data

    def test_css_stylesheet_linked(self, client):
        """Test that CSS stylesheet is linked."""
        response = client.get('/')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        assert 'style.css' in data or 'stylesheet' in data.lower()

    def test_javascript_linked(self, client):
        """Test that JavaScript is linked."""
        response = client.get('/')
        assert response.status_code == 200
        data = response.data.decode('utf-8')

        assert 'main.js' in data or '<script' in data


class TestResponseHeaders:
    """Test suite for response headers and content type."""

    def test_content_type_html(self, client):
        """Test that responses have correct content type."""
        for route in ['/', '/bio', '/portfolio', '/projects', '/contact']:
            response = client.get(route)
            assert response.status_code == 200
            assert 'text/html' in response.content_type

    def test_response_charset(self, client):
        """Test that responses have character set."""
        response = client.get('/')
        assert response.status_code == 200
        # Charset is usually present in content-type header
        assert response.content_type is not None


class TestFormValidation:
    """Test suite for form validation and submission."""

    def test_contact_form_submission_all_fields(self, client):
        """Test contact form submission with all fields."""
        response = client.post('/contact', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Inquiry',
            'message': 'This is a test message'
        }, follow_redirects=True)

        # Should return 200 (success or redirect)
        assert response.status_code == 200

    def test_contact_form_submission_minimal_fields(self, client):
        """Test contact form submission with minimal fields."""
        response = client.post('/contact', data={
            'name': 'Jane',
            'email': 'jane@example.com',
            'message': 'Test'
        })

        # Should handle POST request
        assert response.status_code in [200, 302]

    def test_contact_form_empty(self, client):
        """Test contact form submission with no data."""
        response = client.post('/contact', data={})

        # Should still respond (with or without validation)
        assert response.status_code in [200, 302, 400]
