'use client';

import React from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { useCartStore } from '@/stores/useCartStore';
import { useCompareStore } from '@/stores/useCompareStore';
import { mockProducts } from '@/services/mockData';
import { formatPrice } from '@/lib/utils';
import { ShoppingCart, Scale, Star, Check, Zap } from 'lucide-react';

export default function ProductGridSection() {
  const { locale, t } = useLanguage();
  const addItem = useCartStore((state) => state.addItem);
  const { addToCompare, isInCompare } = useCompareStore();

  return (
    <section className="py-10 bg-slate-50/60 border-t border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <Zap className="w-5 h-5 text-amber-500 fill-amber-500" />
              <h2 className="text-xl sm:text-2xl font-black text-petrol-900">
                {t('featuredProductsTitle')}
              </h2>
            </div>
            <p className="text-xs text-slate-500">{t('featuredProductsSubtitle')}</p>
          </div>

          <Link
            href="/catalog"
            className="text-xs font-bold text-sky-700 hover:text-sky-900 underline underline-offset-4"
          >
            {t('viewAll')} &rarr;
          </Link>
        </div>

        {/* 4-Column Product Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {mockProducts.map((product) => {
            const inCompare = isInCompare(product.id);

            return (
              <div
                key={product.id}
                className="bg-white rounded-2xl border border-slate-200/90 shadow-subtle hover:shadow-hover hover:border-petrol-300 transition-all duration-300 flex flex-col justify-between overflow-hidden group"
              >
                <div>
                  {/* Image & Badges */}
                  <div className="relative h-48 w-full p-4 flex items-center justify-center bg-white border-b border-slate-100 overflow-hidden">
                    {/* Top Badges */}
                    <div className="absolute top-3 start-3 z-10 flex flex-col gap-1.5">
                      {product.discountPercent && (
                        <span className="px-2 py-0.5 rounded-md bg-rose-600 text-white text-[11px] font-black shadow-xs">
                          -{product.discountPercent}%
                        </span>
                      )}
                      {product.isHot && (
                        <span className="px-2 py-0.5 rounded-md bg-amber-500 text-white text-[10px] font-extrabold uppercase">
                          HOT
                        </span>
                      )}
                    </div>

                    {/* Compare Button */}
                    <button
                      onClick={() => addToCompare(product)}
                      className={`absolute top-3 end-3 z-10 p-2 rounded-xl transition-all shadow-xs ${
                        inCompare
                          ? 'bg-sky-600 text-white'
                          : 'bg-white/90 text-slate-500 hover:bg-sky-50 hover:text-sky-700 border border-slate-200'
                      }`}
                      title={t('addToCompare')}
                    >
                      <Scale className="w-4 h-4" />
                    </button>

                    {/* Image */}
                    <img
                      src={product.image}
                      alt={product.name[locale]}
                      className="max-h-full max-w-full object-contain group-hover:scale-105 transition-transform duration-300"
                    />
                  </div>

                  {/* Body Content */}
                  <div className="p-4 space-y-2.5">
                    {/* Brand & Rating */}
                    <div className="flex items-center justify-between text-xs">
                      <span className="font-mono font-bold text-petrol-700 text-[11px] bg-petrol-50 px-2 py-0.5 rounded border border-petrol-100">
                        {product.brand}
                      </span>
                      <div className="flex items-center gap-1 text-amber-500">
                        <Star className="w-3.5 h-3.5 fill-amber-400" />
                        <span className="text-slate-700 font-bold text-[11px]">{product.rating}</span>
                        <span className="text-slate-400 text-[10px]">({product.reviewsCount})</span>
                      </div>
                    </div>

                    {/* Product Name */}
                    <Link
                      href={`/product/${product.id}`}
                      className="font-bold text-sm text-petrol-950 hover:text-sky-700 line-clamp-2 leading-snug transition-colors"
                    >
                      {product.name[locale]}
                    </Link>

                    {/* Model Code */}
                    <span className="block text-[11px] font-mono text-slate-400">
                      Model: {product.model}
                    </span>

                    {/* Key Specs Pills */}
                    <div className="flex flex-wrap gap-1 pt-1">
                      {product.specs.slice(0, 2).map((sp, idx) => (
                        <span
                          key={idx}
                          className="text-[10px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded-md"
                        >
                          {sp.value[locale]}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Pricing & Add to Cart */}
                <div className="p-4 pt-2 border-t border-slate-100 bg-slate-50/40">
                  <div className="flex items-baseline justify-between mb-3">
                    <div>
                      <span className="text-base sm:text-lg font-black text-petrol-900 font-mono">
                        {formatPrice(product.price, locale)}
                      </span>
                      {product.oldPrice && (
                        <span className="block text-xs text-slate-400 line-through font-mono">
                          {formatPrice(product.oldPrice, locale)}
                        </span>
                      )}
                    </div>

                    <span className="text-[10px] text-emerald-600 font-bold flex items-center gap-0.5">
                      <Check className="w-3 h-3" />
                      {t('inStock')}
                    </span>
                  </div>

                  <button
                    onClick={() => addItem(product, 1)}
                    className="w-full py-2.5 px-3 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs flex items-center justify-center gap-2 shadow-xs hover:shadow transition-all active:scale-95"
                  >
                    <ShoppingCart className="w-4 h-4 text-sky-300" />
                    <span>{t('addToCart')}</span>
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
