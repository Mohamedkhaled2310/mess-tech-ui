'use client';

import React from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { mockCategories } from '@/services/mockData';
import { ArrowLeft, ArrowRight } from 'lucide-react';

export default function CategoryBannerGrids() {
  const { locale, dir, t } = useLanguage();

  // Grid 1: Switches, WiFi, Storage
  const grid1 = mockCategories.slice(0, 3);
  // Grid 2: UPS, Attendance, Screens
  const grid2 = mockCategories.slice(3, 6);

  const renderBannerCard = (cat: typeof mockCategories[0]) => (
    <div
      key={cat.id}
      className="group relative rounded-2xl overflow-hidden border border-slate-200/80 bg-white shadow-subtle hover:shadow-hover transition-all duration-300 flex flex-col"
    >
      {/* Banner Visual Area */}
      <div className="relative h-44 sm:h-48 w-full overflow-hidden bg-slate-100">
        <img
          src={cat.image}
          alt={cat.title[locale]}
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-petrol-950/60 via-transparent to-transparent" />
        <span className="absolute top-3 end-3 px-2.5 py-1 rounded-full bg-white/90 text-petrol-800 text-[11px] font-bold shadow-sm backdrop-blur-xs">
          {cat.count} {t('items')}
        </span>
      </div>

      {/* Banner Content Area */}
      <div className="p-4 sm:p-5 flex-1 flex flex-col justify-between">
        <div>
          <h3 className="font-extrabold text-base sm:text-lg text-petrol-900 mb-1 group-hover:text-sky-700 transition-colors">
            {cat.title[locale]}
          </h3>
          <p className="text-xs text-slate-500 line-clamp-2 leading-relaxed mb-4">
            {cat.desc[locale]}
          </p>
        </div>

        <Link
          href={`/catalog?category=${cat.slug}`}
          className="inline-flex items-center justify-between w-full px-4 py-2.5 rounded-xl bg-petrol-50 hover:bg-petrol-700 text-petrol-800 hover:text-white font-bold text-xs transition-all group/btn"
        >
          <span>{t('shopNow')}</span>
          {dir === 'rtl' ? (
            <ArrowLeft className="w-3.5 h-3.5 group-hover/btn:-translate-x-1 transition-transform" />
          ) : (
            <ArrowRight className="w-3.5 h-3.5 group-hover/btn:translate-x-1 transition-transform" />
          )}
        </Link>
      </div>
    </div>
  );

  return (
    <section className="py-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
      {/* Section Header */}
      <div className="text-center max-w-2xl mx-auto space-y-2">
        <span className="text-xs font-bold uppercase tracking-wider text-sky-600 bg-sky-50 px-3 py-1 rounded-full border border-sky-100">
          MESS TECH NETWORKS
        </span>
        <h2 className="text-2xl sm:text-3xl font-black text-petrol-900 tracking-tight">
          {t('categoryGridsTitle')}
        </h2>
        <p className="text-xs sm:text-sm text-slate-500">{t('categoryGridsSubtitle')}</p>
      </div>

      {/* Grid 1: Switches / WiFi / Storage */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {grid1.map((cat) => renderBannerCard(cat))}
      </div>

      {/* Grid 2: UPS / Attendance / Screens */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {grid2.map((cat) => renderBannerCard(cat))}
      </div>
    </section>
  );
}
