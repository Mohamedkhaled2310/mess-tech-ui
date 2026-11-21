import type { Metadata } from 'next';
import './globals.css';
import { LanguageProvider } from '@/context/LanguageContext';
import QueryProvider from '@/components/providers/QueryProvider';
import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';
import CartDrawer from '@/components/cart/CartDrawer';
import CompareDrawer from '@/components/compare/CompareDrawer';

export const metadata: Metadata = {
  title: 'MESS TECH | متجر حلول وأنظمة الشبكات في مصر',
  description: 'المتجر الرائد لتوريد سويتشات Cisco و MikroTik، راوترات، حلول واي فاي، وسيرفرات تخزين NAS في مصر والدفع عند الاستلام COD.',
  keywords: ['سويتشات سيسكو', 'MikroTik', 'Cisco Catalyst', 'شبكات مصر', 'UniFi AP', 'Synology NAS', 'APC UPS'],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ar" dir="rtl">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="min-h-screen flex flex-col bg-slate-50 antialiased font-cairo">
        <LanguageProvider>
          <QueryProvider>
            <Navbar />
            <main className="flex-1">{children}</main>
            <CartDrawer />
            <CompareDrawer />
            <Footer />
          </QueryProvider>
        </LanguageProvider>
      </body>
    </html>
  );
}
