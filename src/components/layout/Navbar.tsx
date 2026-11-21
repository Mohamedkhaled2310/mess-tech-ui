'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { useCartStore } from '@/stores/useCartStore';
import { useCompareStore } from '@/stores/useCompareStore';
import {
  Search,
  ShoppingCart,
  Scale,
  PhoneCall,
  Globe,
  Menu,
  X,
  ChevronDown,
  Layers,
  ShieldCheck,
  CheckCircle2,
} from 'lucide-react';

export default function Navbar() {
  const { locale, toggleLanguage, t } = useLanguage();
  const totalCartItems = useCartStore((state) => state.getTotalItems());
  const toggleCart = useCartStore((state) => state.toggleCart);
  const compareCount = useCompareStore((state) => state.items.length);
  const toggleCompare = useCompareStore((state) => state.toggleCompare);

  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');

  const navCategories = [
    { label: t('nav_home'), href: '/' },
    { label: t('nav_switches'), href: '/catalog?category=switches' },
    { label: t('nav_wifi'), href: '/catalog?category=wifi' },
    { label: t('nav_storage'), href: '/catalog?category=storage' },
    { label: t('nav_ups'), href: '/catalog?category=ups' },
    { label: t('nav_voip'), href: '/catalog?category=voip' },
    { label: t('nav_attendance'), href: '/catalog?category=attendance' },
    { label: t('nav_screens'), href: '/catalog?category=screens' },
    { label: t('nav_passive'), href: '/catalog?category=passive' },
  ];

  return (
    <header className="w-full sticky top-0 z-40 bg-white shadow-subtle border-b border-slate-200">
      {/* Top Banner Bar */}
      <div className="bg-petrol-800 text-white text-xs py-2 px-4 border-b border-petrol-700">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-6">
            <div className="flex items-center gap-1.5 text-petrol-200 font-mono">
              <PhoneCall className="w-3.5 h-3.5 text-sky-400" />
              <span>{t('hotline')}</span>
            </div>
            <span className="hidden md:inline text-petrol-300">|</span>
            <span className="hidden md:inline text-petrol-200">{t('salesSupport')}</span>
          </div>

          <div className="flex items-center gap-4">
            <span className="hidden sm:flex items-center gap-1 text-emerald-300 text-[11px]">
              <CheckCircle2 className="w-3.5 h-3.5" />
              {t('officialAgent')}
            </span>

            {/* Language Switcher */}
            <button
              onClick={toggleLanguage}
              className="flex items-center gap-1.5 px-2.5 py-1 rounded bg-petrol-700 hover:bg-petrol-600 text-white font-medium transition-colors border border-petrol-600 text-xs"
              title="Change Language"
            >
              <Globe className="w-3.5 h-3.5 text-sky-300" />
              <span>{t('langSwitch')}</span>
            </button>
          </div>
        </div>
      </div>

      {/* Main Brand & Search Bar */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <div className="flex items-center justify-between gap-4">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2.5 shrink-0">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-petrol-700 to-petrol-900 flex items-center justify-center text-white font-extrabold text-xl shadow-md border border-petrol-600">
              M
            </div>
            <div className="flex flex-col">
              <span className="font-extrabold text-xl tracking-tight text-petrol-900 leading-none">
                MESS <span className="text-sky-600">TECH</span>
              </span>
              <span className="text-[10px] text-slate-500 font-medium tracking-wide">
                NETWORKING SYSTEMS
              </span>
            </div>
          </Link>

          {/* Search Input with Category Select */}
          <div className="hidden lg:flex flex-1 max-w-2xl mx-6">
            <div className="w-full flex items-center rounded-xl border-2 border-petrol-600/30 hover:border-petrol-600 focus-within:border-petrol-600 focus-within:ring-2 focus-within:ring-petrol-100 transition-all bg-slate-50 overflow-hidden">
              <div className="flex items-center gap-1.5 px-3 py-2 text-xs text-slate-600 border-e border-slate-200 bg-white shrink-0 font-medium">
                <Layers className="w-3.5 h-3.5 text-petrol-600" />
                <span>{t('allCategories')}</span>
                <ChevronDown className="w-3 h-3 text-slate-400" />
              </div>

              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder={t('searchPlaceholder')}
                className="w-full px-4 py-2 text-xs bg-transparent focus:outline-none text-slate-800 placeholder-slate-400"
              />

              <button className="bg-petrol-700 hover:bg-petrol-800 text-white px-5 py-2.5 flex items-center justify-center transition-colors">
                <Search className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Actions: Compare + Cart */}
          <div className="flex items-center gap-2.5 sm:gap-3">
            {/* Compare Button */}
            <button
              onClick={toggleCompare}
              className="relative p-2.5 rounded-xl border border-slate-200 text-slate-700 hover:bg-petrol-50 hover:text-petrol-700 transition-colors flex items-center gap-2"
              title={t('compare')}
            >
              <Scale className="w-5 h-5" />
              <span className="hidden sm:inline text-xs font-semibold">{t('compare')}</span>
              {compareCount > 0 && (
                <span className="absolute -top-1.5 -end-1.5 w-5 h-5 rounded-full bg-sky-600 text-white text-[11px] font-bold flex items-center justify-center shadow-sm">
                  {compareCount}
                </span>
              )}
            </button>

            {/* Cart Button */}
            <button
              onClick={toggleCart}
              className="relative p-2.5 sm:px-4 sm:py-2.5 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-semibold transition-all flex items-center gap-2.5 shadow-sm hover:shadow"
              title={t('myCart')}
            >
              <ShoppingCart className="w-5 h-5 text-sky-300" />
              <span className="hidden sm:inline text-xs font-bold">{t('myCart')}</span>
              <span className="w-5 h-5 rounded-full bg-amber-400 text-petrol-900 text-[11px] font-black flex items-center justify-center">
                {totalCartItems}
              </span>
            </button>

            {/* Mobile Hamburger */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="lg:hidden p-2 rounded-xl text-slate-700 hover:bg-slate-100"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>

        {/* Mobile Search Bar */}
        <div className="mt-3 lg:hidden">
          <div className="flex items-center rounded-xl border border-slate-300 bg-slate-50 overflow-hidden">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder={t('searchPlaceholder')}
              className="w-full px-3 py-2 text-xs bg-transparent focus:outline-none"
            />
            <button className="bg-petrol-700 text-white p-2.5">
              <Search className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* Categories Navigation Bar */}
      <nav className="hidden lg:block bg-petrol-50/80 border-t border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <ul className="flex items-center gap-1 overflow-x-auto py-1.5 scrollbar-none">
            {navCategories.map((item, index) => (
              <li key={index}>
                <Link
                  href={item.href}
                  className={`px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all inline-block whitespace-nowrap ${
                    index === 0
                      ? 'bg-petrol-700 text-white shadow-xs'
                      : 'text-petrol-900 hover:bg-white hover:text-sky-700'
                  }`}
                >
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </nav>

      {/* Mobile Drawer Navigation */}
      {mobileMenuOpen && (
        <div className="lg:hidden bg-white border-t border-slate-200 p-4 shadow-xl">
          <div className="space-y-1">
            {navCategories.map((item, index) => (
              <Link
                key={index}
                href={item.href}
                onClick={() => setMobileMenuOpen(false)}
                className="block px-3 py-2.5 rounded-lg text-sm font-bold text-petrol-900 hover:bg-petrol-50"
              >
                {item.label}
              </Link>
            ))}
          </div>
        </div>
      )}
    </header>
  );
}
