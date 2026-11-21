'use client';

import React, { useState, useMemo } from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { useCartStore } from '@/stores/useCartStore';
import { useCompareStore } from '@/stores/useCompareStore';
import { mockProducts, mockCategories } from '@/services/mockData';
import { formatPrice } from '@/lib/utils';
import { Filter, ShoppingCart, Scale, Star, Check, RotateCcw } from 'lucide-react';

export default function CatalogPage() {
  const { locale, t } = useLanguage();
  const addItem = useCartStore((state) => state.addItem);
  const { addToCompare, isInCompare } = useCompareStore();

  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [selectedBrand, setSelectedBrand] = useState<string>('all');
  const [sortBy, setSortBy] = useState<'featured' | 'price-asc' | 'price-desc'>('featured');

  const brands = useMemo(() => {
    return Array.from(new Set(mockProducts.map((p) => p.brand)));
  }, []);

  const filteredProducts = useMemo(() => {
    return mockProducts
      .filter((p) => (selectedCategory === 'all' ? true : p.category === selectedCategory))
      .filter((p) => (selectedBrand === 'all' ? true : p.brand === selectedBrand))
      .sort((a, b) => {
        if (sortBy === 'price-asc') return a.price - b.price;
        if (sortBy === 'price-desc') return b.price - a.price;
        return (b.isFeatured ? 1 : 0) - (a.isFeatured ? 1 : 0);
      });
  }, [selectedCategory, selectedBrand, sortBy]);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">
      {/* Breadcrumb & Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-4">
        <div>
          <nav className="text-xs text-slate-500 mb-1 flex items-center gap-1.5">
            <Link href="/" className="hover:text-petrol-700">{t('nav_home')}</Link>
            <span>/</span>
            <span className="text-petrol-900 font-bold">{t('featuredProductsTitle')}</span>
          </nav>
          <h1 className="text-2xl font-black text-petrol-900">
            {t('featuredProductsTitle')}
            <span className="text-sm font-normal text-slate-400 ms-2 font-mono">
              ({filteredProducts.length} {t('items')})
            </span>
          </h1>
        </div>

        {/* Sort Select */}
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500 font-medium">ترتيب حسب:</span>
          <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value as any)}
            className="text-xs font-bold text-petrol-900 bg-white border border-slate-200 rounded-xl px-3 py-2 focus:outline-none focus:ring-2 focus:ring-petrol-200"
          >
            <option value="featured">المميز والأحدث</option>
            <option value="price-asc">السعر: من الأقل للأعلى</option>
            <option value="price-desc">السعر: من الأعلى للأقل</option>
          </select>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
        {/* Filters Sidebar */}
        <aside className="space-y-6 bg-white p-5 rounded-2xl border border-slate-200 shadow-subtle h-fit">
          <div className="flex items-center justify-between pb-3 border-b border-slate-100">
            <div className="flex items-center gap-2 font-extrabold text-sm text-petrol-900">
              <Filter className="w-4 h-4 text-sky-600" />
              <span>تصفية النتائج</span>
            </div>
            <button
              onClick={() => {
                setSelectedCategory('all');
                setSelectedBrand('all');
              }}
              className="text-[11px] text-slate-400 hover:text-rose-600 flex items-center gap-1"
            >
              <RotateCcw className="w-3 h-3" />
              <span>إعادة ضبط</span>
            </button>
          </div>

          {/* Categories */}
          <div>
            <h4 className="font-bold text-xs text-slate-800 mb-2.5">الأقسام</h4>
            <div className="space-y-1 text-xs">
              <button
                onClick={() => setSelectedCategory('all')}
                className={`w-full text-start px-2.5 py-1.5 rounded-lg font-medium transition-colors ${
                  selectedCategory === 'all'
                    ? 'bg-petrol-50 text-petrol-900 font-bold'
                    : 'text-slate-600 hover:bg-slate-50'
                }`}
              >
                جميع الأقسام ({mockProducts.length})
              </button>
              {mockCategories.map((cat) => (
                <button
                  key={cat.id}
                  onClick={() => setSelectedCategory(cat.slug)}
                  className={`w-full text-start px-2.5 py-1.5 rounded-lg font-medium transition-colors ${
                    selectedCategory === cat.slug
                      ? 'bg-petrol-50 text-petrol-900 font-bold'
                      : 'text-slate-600 hover:bg-slate-50'
                  }`}
                >
                  {cat.title[locale]}
                </button>
              ))}
            </div>
          </div>

          {/* Brands */}
          <div className="pt-3 border-t border-slate-100">
            <h4 className="font-bold text-xs text-slate-800 mb-2.5">العلامة التجارية</h4>
            <div className="space-y-1 text-xs">
              <button
                onClick={() => setSelectedBrand('all')}
                className={`w-full text-start px-2.5 py-1.5 rounded-lg font-medium transition-colors ${
                  selectedBrand === 'all'
                    ? 'bg-petrol-50 text-petrol-900 font-bold'
                    : 'text-slate-600 hover:bg-slate-50'
                }`}
              >
                جميع العلامات
              </button>
              {brands.map((b) => (
                <button
                  key={b}
                  onClick={() => setSelectedBrand(b)}
                  className={`w-full text-start px-2.5 py-1.5 rounded-lg font-medium transition-colors ${
                    selectedBrand === b
                      ? 'bg-petrol-50 text-petrol-900 font-bold'
                      : 'text-slate-600 hover:bg-slate-50'
                  }`}
                >
                  {b}
                </button>
              ))}
            </div>
          </div>
        </aside>

        {/* Products Grid */}
        <div className="lg:col-span-3">
          {filteredProducts.length === 0 ? (
            <div className="p-12 text-center bg-white rounded-2xl border border-slate-200">
              <p className="text-slate-500 text-sm">لا توجد منتجات تطابق الفلاتر المحددة</p>
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredProducts.map((product) => {
                const inCompare = isInCompare(product.id);

                return (
                  <div
                    key={product.id}
                    className="bg-white rounded-2xl border border-slate-200/90 shadow-subtle hover:shadow-hover hover:border-petrol-300 transition-all duration-300 flex flex-col justify-between overflow-hidden group"
                  >
                    <div>
                      {/* Image Area */}
                      <div className="relative h-48 w-full p-4 flex items-center justify-center bg-white border-b border-slate-100">
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

                        <img
                          src={product.image}
                          alt={product.name[locale]}
                          className="max-h-full max-w-full object-contain group-hover:scale-105 transition-transform"
                        />
                      </div>

                      {/* Content */}
                      <div className="p-4 space-y-2">
                        <span className="font-mono font-bold text-petrol-700 text-[11px] bg-petrol-50 px-2 py-0.5 rounded border border-petrol-100">
                          {product.brand}
                        </span>

                        <Link
                          href={`/product/${product.id}`}
                          className="font-bold text-sm text-petrol-950 hover:text-sky-700 line-clamp-2 leading-snug block"
                        >
                          {product.name[locale]}
                        </Link>

                        <span className="block text-[11px] font-mono text-slate-400">
                          {product.model}
                        </span>
                      </div>
                    </div>

                    {/* Price and Cart */}
                    <div className="p-4 pt-2 border-t border-slate-100 bg-slate-50/40">
                      <div className="flex items-baseline justify-between mb-3">
                        <span className="text-base font-black text-petrol-900 font-mono">
                          {formatPrice(product.price, locale)}
                        </span>
                        <span className="text-[10px] text-emerald-600 font-bold flex items-center gap-0.5">
                          <Check className="w-3 h-3" />
                          {t('inStock')}
                        </span>
                      </div>

                      <button
                        onClick={() => addItem(product, 1)}
                        className="w-full py-2.5 px-3 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs flex items-center justify-center gap-2 transition-all active:scale-95 shadow-xs"
                      >
                        <ShoppingCart className="w-4 h-4 text-sky-300" />
                        <span>{t('addToCart')}</span>
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
