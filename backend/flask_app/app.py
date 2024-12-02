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

# Tool model
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    website = db.Column(db.String(200))
    rating = db.Column(db.Float, default=0.0)

# Create database tables
def init_db():
    try:
        with app.app_context():
            db.create_all()
            logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Flask API is running'}), 200

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
        logger.error(f"Error fetching tools: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/tools', methods=['POST'])
def add_tool():
    try:
        data = request.json
        new_tool = Tool(
            name=data['name'],
            description=data['description'],
            category=data['category'],
            website=data.get('website', ''),
            rating=data.get('rating', 0.0)
        )
        db.session.add(new_tool)
        db.session.commit()
        return jsonify({'message': 'Tool added successfully'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        logger.error(f"Error adding tool: {e}")
        return jsonify({'error': 'Internal server error'}), 500

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
        logger.error(f"Error fetching tool {tool_id}: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    init_db()  # Initialize database tables
    app.run(debug=True, port=5000)
