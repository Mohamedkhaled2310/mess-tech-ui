'use client';

import React from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { useCompareStore } from '@/stores/useCompareStore';
import { formatPrice } from '@/lib/utils';
import { Scale, X, ArrowLeft, ArrowRight, Trash2 } from 'lucide-react';

export default function CompareDrawer() {
  const { locale, dir, t } = useLanguage();
  const { items, isOpen, closeCompare, removeFromCompare, clearCompare } = useCompareStore();

  if (!isOpen || items.length === 0) return null;

  return (
    <div className="fixed bottom-0 inset-x-0 z-40 bg-white border-t-2 border-petrol-700 shadow-2xl p-4 animate-in slide-in-from-bottom duration-200">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        {/* Info */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-petrol-100 text-petrol-800 flex items-center justify-center">
            <Scale className="w-5 h-5" />
          </div>
          <div>
            <h4 className="font-extrabold text-sm text-petrol-900">{t('compare')} ({items.length}/4)</h4>
            <p className="text-xs text-slate-500">اختر حتى 4 أجهزة لمقارنة المواصفات والأسعار جنباً إلى جنب</p>
          </div>
        </div>

        {/* Selected Products Thumbnails */}
        <div className="flex items-center gap-3 overflow-x-auto py-1">
          {items.map((prod) => (
            <div
              key={prod.id}
              className="relative w-20 h-20 rounded-xl border border-slate-200 bg-slate-50 p-1.5 flex flex-col items-center justify-center shrink-0 group"
            >
              <button
                onClick={() => removeFromCompare(prod.id)}
                className="absolute -top-1.5 -end-1.5 w-5 h-5 rounded-full bg-rose-500 text-white flex items-center justify-center shadow-xs hover:bg-rose-600 transition-colors"
                title={t('removeFromCompare')}
              >
                <X className="w-3 h-3" />
              </button>
              <img src={prod.image} alt={prod.name[locale]} className="max-h-12 max-w-full object-contain mb-1" />
              <span className="text-[9px] font-mono font-bold text-petrol-800 line-clamp-1">{prod.model}</span>
            </div>
          ))}
        </div>

        {/* Action Buttons */}
        <div className="flex items-center gap-2.5">
          <button
            onClick={clearCompare}
            className="px-3 py-2 text-xs font-semibold text-slate-500 hover:text-rose-600 flex items-center gap-1"
          >
            <Trash2 className="w-3.5 h-3.5" />
            <span>مسح الكل</span>
          </button>

          <Link
            href="/compare"
            onClick={closeCompare}
            className="px-5 py-2.5 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs flex items-center gap-2 shadow-sm"
          >
            <span>{t('compareNow')}</span>
            {dir === 'rtl' ? <ArrowLeft className="w-4 h-4" /> : <ArrowRight className="w-4 h-4" />}
          </Link>
        </div>
      </div>
    </div>
  );
}
