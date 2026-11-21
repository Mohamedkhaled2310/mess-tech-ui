'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useLanguage } from '@/context/LanguageContext';
import {
  LayoutDashboard,
  ShoppingBag,
  Package,
  Users,
  Layers,
  Settings,
  Store,
  ChevronLeft,
  ChevronRight,
} from 'lucide-react';

export default function AdminSidebar() {
  const pathname = usePathname();
  const { dir } = useLanguage();

  const links = [
    { label: 'نظرة عامة', href: '/admin/dashboard', icon: <LayoutDashboard className="w-4 h-4" /> },
    { label: 'إدارة الطلبات', href: '/admin/orders', icon: <ShoppingBag className="w-4 h-4" /> },
    { label: 'المنتجات والمخزون', href: '/admin/products', icon: <Package className="w-4 h-4" /> },
    { label: 'سجل العملاء', href: '/admin/customers', icon: <Users className="w-4 h-4" /> },
    { label: 'التصنيفات والأقسام', href: '/admin/categories', icon: <Layers className="w-4 h-4" /> },
    { label: 'إعدادات الشحن والمتجر', href: '/admin/settings', icon: <Settings className="w-4 h-4" /> },
  ];

  return (
    <aside className="w-64 bg-petrol-950 text-white p-5 flex flex-col justify-between shrink-0 min-h-screen border-e border-petrol-900">
      <div className="space-y-6">
        {/* Brand */}
        <div className="flex items-center gap-2.5 pb-4 border-b border-petrol-800">
          <div className="w-8 h-8 rounded-lg bg-petrol-700 flex items-center justify-center font-black text-white text-base">
            M
          </div>
          <div>
            <span className="font-extrabold text-sm block leading-none">MESS TECH</span>
            <span className="text-[10px] text-sky-400 font-mono">ADMIN PANEL</span>
          </div>
        </div>

        {/* Links */}
        <nav className="space-y-1 text-xs">
          {links.map((link) => {
            const isActive = pathname === link.href || pathname.startsWith(link.href + '/');
            return (
              <Link
                key={link.href}
                href={link.href}
                className={`flex items-center justify-between px-3.5 py-2.5 rounded-xl font-bold transition-colors ${
                  isActive
                    ? 'bg-petrol-700 text-white shadow-sm'
                    : 'text-slate-300 hover:bg-petrol-900 hover:text-white'
                }`}
              >
                <div className="flex items-center gap-2.5">
                  {link.icon}
                  <span>{link.label}</span>
                </div>
                {dir === 'rtl' ? <ChevronLeft className="w-3.5 h-3.5" /> : <ChevronRight className="w-3.5 h-3.5" />}
              </Link>
            );
          })}
        </nav>
      </div>

      {/* Back to store */}
      <div className="pt-4 border-t border-petrol-800">
        <Link
          href="/"
          className="flex items-center gap-2 px-3 py-2 rounded-xl text-xs font-bold text-sky-300 hover:bg-petrol-900 transition-colors"
        >
          <Store className="w-4 h-4" />
          <span>العودة للمتجر العام</span>
        </Link>
      </div>
    </aside>
  );
}
