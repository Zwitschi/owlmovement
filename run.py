"""
Main application entry point
"""

from flask import Flask, render_template, request, jsonify
from config import Config
from app.data import (
    FEATURED_PROJECTS,
    PORTFOLIO_ITEMS,
    PROJECTS,
    SOCIAL_MEDIA,
    PAGE_METADATA,
)


def create_app():
    """Application factory"""
    app = Flask(__name__, template_folder='app/templates',
                static_folder='app/static')
    app.config.from_object(Config)

    # Routes
    @app.route('/')
    def index():
        """Home page"""
        meta = PAGE_METADATA.get('index', {})
        return render_template('index.html',
                               title=meta.get('title', 'Home'),
                               meta=meta,
                               featured_projects=FEATURED_PROJECTS,
                               social_media=SOCIAL_MEDIA)

    @app.route('/bio')
    def bio():
        """Biography page"""
        meta = PAGE_METADATA.get('bio', {})
        return render_template('bio.html',
                               title=meta.get('title', 'About'),
                               meta=meta,
                               featured_projects=FEATURED_PROJECTS,
                               social_media=SOCIAL_MEDIA)

    @app.route('/portfolio')
    def portfolio():
        """Portfolio page"""
        meta = PAGE_METADATA.get('portfolio', {})
        return render_template('portfolio.html',
                               title=meta.get('title', 'Portfolio'),
                               meta=meta,
                               portfolio_items=PORTFOLIO_ITEMS,
                               social_media=SOCIAL_MEDIA)

    @app.route('/projects')
    def projects():
        """Projects page"""
        meta = PAGE_METADATA.get('projects', {})
        return render_template('projects.html',
                               title=meta.get('title', 'Projects'),
                               meta=meta,
                               projects=PROJECTS,
                               featured_projects=FEATURED_PROJECTS,
                               social_media=SOCIAL_MEDIA)

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        """Contact page"""
        meta = PAGE_METADATA.get('contact', {})
        if request.method == 'POST':
            # TODO: Save message to database or send email
            return jsonify({'status': 'success', 'message': 'Message sent successfully!'})

        return render_template('contact.html',
                               title=meta.get('title', 'Contact'),
                               meta=meta,
                               social_media=SOCIAL_MEDIA)

    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(error):
        """Handle 500 errors"""
        return render_template('500.html'), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
