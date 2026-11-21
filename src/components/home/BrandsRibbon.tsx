'use client';

import React from 'react';
import { useLanguage } from '@/context/LanguageContext';
import { mockBrands } from '@/services/mockData';
import { Award } from 'lucide-react';

export default function BrandsRibbon() {
  const { t } = useLanguage();

  return (
    <section className="py-10 bg-white border-t border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-lg sm:text-xl font-black text-petrol-900 flex items-center gap-2">
              <Award className="w-5 h-5 text-sky-600" />
              <span>{t('brandsTitle')}</span>
            </h2>
            <p className="text-xs text-slate-500">{t('brandsSubtitle')}</p>
          </div>
        </div>

        {/* Brand Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3 sm:gap-4">
          {mockBrands.map((brand, idx) => (
            <div
              key={idx}
              className="p-3.5 rounded-xl border border-slate-200/90 bg-slate-50/50 hover:bg-white hover:border-petrol-400 hover:shadow-subtle transition-all flex flex-col items-center justify-center text-center group"
            >
              <span className="font-mono font-black text-sm text-petrol-900 group-hover:text-sky-600 transition-colors tracking-tight">
                {brand.logoText}
              </span>
              <span className="text-[9px] font-bold text-slate-400 mt-1 uppercase tracking-wider">
                {brand.tier}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
