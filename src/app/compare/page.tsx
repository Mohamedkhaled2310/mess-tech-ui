'use client';

import React from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { useCompareStore } from '@/stores/useCompareStore';
import { formatPrice } from '@/lib/utils';
import { Scale, X, ShoppingCart, Trash2 } from 'lucide-react';
import { useCartStore } from '@/stores/useCartStore';

export default function ComparePage() {
  const { locale, t } = useLanguage();
  const { items, removeFromCompare, clearCompare } = useCompareStore();
  const addItem = useCartStore((state) => state.addItem);

  if (items.length === 0) {
    return (
      <div className="max-w-xl mx-auto py-20 px-4 text-center space-y-4">
        <div className="w-16 h-16 rounded-full bg-petrol-50 flex items-center justify-center mx-auto text-petrol-700">
          <Scale className="w-8 h-8" />
        </div>
        <h2 className="text-xl font-bold text-petrol-900">لا توجد أجهزة في قائمة المقارنة</h2>
        <p className="text-xs text-slate-500">
          تصفح الأجهزة واضغط على أيقونة المقارنة للمفاضلة بين الموديلات والمواصفات الفنية
        </p>
        <Link
          href="/catalog"
          className="inline-block px-5 py-2.5 rounded-xl bg-petrol-700 text-white font-bold text-xs"
        >
          تصفح المنتجات الآن
        </Link>
      </div>
    );
  }

  // Gather unique spec keys across all products
  const specKeys = Array.from(
    new Set(items.flatMap((p) => p.specs.map((sp) => sp.key.ar)))
  );

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      <div className="flex items-center justify-between border-b border-slate-200 pb-4">
        <div>
          <h1 className="text-2xl font-black text-petrol-900 flex items-center gap-2">
            <Scale className="w-6 h-6 text-sky-600" />
            <span>{t('compare')} ({items.length}/4)</span>
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            مقارنة تقنية تفصيلية بين الموديلات المختارة لتحديد الأنسب لشبكتك
          </p>
        </div>

        <button
          onClick={clearCompare}
          className="px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-rose-600 hover:bg-rose-50 flex items-center gap-1.5 transition-colors"
        >
          <Trash2 className="w-3.5 h-3.5" />
          <span>مسح المقارنة</span>
        </button>
      </div>

      {/* Comparison Matrix Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-subtle overflow-x-auto">
        <table className="w-full text-xs">
          <thead>
            <tr className="border-b border-slate-200 bg-slate-50/80">
              <th className="p-4 text-start font-bold text-slate-500 w-44">المواصفات</th>
              {items.map((prod) => (
                <th key={prod.id} className="p-4 text-start min-w-[220px]">
                  <div className="relative space-y-2">
                    <button
                      onClick={() => removeFromCompare(prod.id)}
                      className="absolute -top-1 -end-1 p-1 text-slate-400 hover:text-rose-600"
                    >
                      <X className="w-4 h-4" />
                    </button>
                    <img src={prod.image} alt={prod.name[locale]} className="h-24 mx-auto object-contain" />
                    <span className="font-mono text-[11px] font-bold text-sky-700 block">
                      {prod.brand} • {prod.model}
                    </span>
                    <h4 className="font-bold text-xs text-petrol-950 line-clamp-2 leading-snug">
                      {prod.name[locale]}
                    </h4>
                    <span className="text-sm font-black text-petrol-900 font-mono block">
                      {formatPrice(prod.price, locale)}
                    </span>
                    <button
                      onClick={() => addItem(prod, 1)}
                      className="w-full py-2 px-3 rounded-lg bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-[11px] flex items-center justify-center gap-1.5 transition-all shadow-xs"
                    >
                      <ShoppingCart className="w-3.5 h-3.5" />
                      <span>{t('addToCart')}</span>
                    </button>
                  </div>
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {specKeys.map((key) => (
              <tr key={key} className="hover:bg-slate-50/50">
                <td className="p-4 font-bold text-slate-700 bg-slate-50/40">{key}</td>
                {items.map((prod) => {
                  const spec = prod.specs.find((s) => s.key.ar === key);
                  return (
                    <td key={prod.id} className="p-4 font-medium text-slate-800">
                      {spec ? spec.value[locale] : '—'}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
