from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = Flask(__name__)
CORS(app)

# Ensure instance folder exists
os.makedirs('instance', exist_ok=True)

# Configure SQLite database with absolute path
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'tools.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    website = db.Column(db.String(200))
    rating = db.Column(db.Float, default=0.0)

def init_db():
    with app.app_context():
        db.create_all()
        
        # Add sample data if the database is empty
        if Tool.query.count() == 0:
            sample_tools = [
                Tool(
                    name='Webflow',
                    description='Professional no-code website builder with advanced design capabilities',
                    category='Website Builder',
                    website='https://webflow.com',
                    rating=4.5
                ),
                Tool(
                    name='Bubble',
                    description='Powerful no-code platform for building web applications',
                    category='App Builder',
                    website='https://bubble.io',
                    rating=4.7
                ),
                Tool(
                    name='Zapier',
                    description='Connect your apps and automate workflows',
                    category='Automation',
                    website='https://zapier.com',
                    rating=4.6
                )
            ]
            for tool in sample_tools:
                db.session.add(tool)
            db.session.commit()
            logger.info('Sample data added to database')

@app.route('/')
def index():
    return jsonify({'message': 'No-Code Tools API'})

@app.route('/api/tools', methods=['GET'])
def get_tools():
    try:
        tools = Tool.query.all()
        return jsonify([{
            'id': tool.id,
            'name': tool.name,
            'description': tool.description,
            'category': tool.category,
            'website': tool.website,
            'rating': tool.rating
        } for tool in tools])
    except Exception as e:
        logger.error(f'Error fetching tools: {str(e)}')
        return jsonify({'error': 'Failed to fetch tools'}), 500

@app.route('/api/tools', methods=['POST'])
def add_tool():
    try:
        data = request.get_json()
        new_tool = Tool(
            name=data['name'],
            description=data['description'],
            category=data['category'],
            website=data.get('website'),
            rating=data.get('rating', 0.0)
        )
        db.session.add(new_tool)
        db.session.commit()
        return jsonify({
            'id': new_tool.id,
            'name': new_tool.name,
            'description': new_tool.description,
            'category': new_tool.category,
            'website': new_tool.website,
            'rating': new_tool.rating
        }), 201
    except Exception as e:
        logger.error(f'Error adding tool: {str(e)}')
        return jsonify({'error': 'Failed to add tool'}), 500

@app.route('/api/tools/<int:tool_id>', methods=['GET'])
def get_tool(tool_id):
    try:
        tool = Tool.query.get_or_404(tool_id)
        return jsonify({
            'id': tool.id,
            'name': tool.name,
            'description': tool.description,
            'category': tool.category,
            'website': tool.website,
            'rating': tool.rating
        })
    except Exception as e:
        logger.error(f'Error fetching tool {tool_id}: {str(e)}')
        return jsonify({'error': f'Failed to fetch tool {tool_id}'}), 500

if __name__ == '__main__':
    init_db()  # Initialize database tables
    app.run(debug=True, host='0.0.0.0', port=5000)
