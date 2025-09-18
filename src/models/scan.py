from src.models.user import db
from datetime import datetime

class Scan(db.Model):
    __tablename__ = 'scans'
    
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(200), nullable=False)
    website = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    scan_type = db.Column(db.String(50), nullable=False)  # 'free' or 'deep'
    status = db.Column(db.String(50), default='pending')  # 'pending', 'processing', 'completed', 'failed'
    results = db.Column(db.Text)  # JSON string of analysis results
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'<Scan {self.id}: {self.business_name} - {self.scan_type}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'business_name': self.business_name,
            'website': self.website,
            'email': self.email,
            'scan_type': self.scan_type,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }

