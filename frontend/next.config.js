/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
    domains: ['*'],
  },
  trailingSlash: true,
  reactStrictMode: true,
  poweredByHeader: false,
  generateEtags: false,
  compress: true
}

module.exports = nextConfig
