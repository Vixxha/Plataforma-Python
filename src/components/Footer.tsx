import { Link } from 'lucide-react';
import './Footer.css';

const LinkedinIcon = ({ size = 20 }: { size?: number }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
    <rect x="2" y="9" width="4" height="12"></rect>
    <circle cx="4" cy="4" r="2"></circle>
  </svg>
);

const InstagramIcon = ({ size = 20 }: { size?: number }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
    <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
    <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
  </svg>
);

export const Footer = () => {
  return (
    <footer className="app-footer">
      <div className="footer-content">
        <p className="footer-text">Plataforma desarrollada por <strong>Alexis Ortega</strong></p>
        <div className="social-links">
          <a
            href="https://portafolio-web-alexis.netlify.app"
            target="_blank"
            rel="noopener noreferrer"
            className="social-link"
            title="Portafolio Web"
          >
            <Link size={18} />
            <span>Portafolio</span>
          </a>
          <a
            href="https://www.linkedin.com/in/alexisortegacaruso/"
            target="_blank"
            rel="noopener noreferrer"
            className="social-link"
            title="LinkedIn"
          >
            <LinkedinIcon size={18} />
            <span>LinkedIn</span>
          </a>
          <a
            href="https://www.instagram.com/chopino._/"
            target="_blank"
            rel="noopener noreferrer"
            className="social-link"
            title="Instagram"
          >
            <InstagramIcon size={18} />
            <span>Instagram</span>
          </a>
        </div>
      </div>
    </footer>
  );
};
