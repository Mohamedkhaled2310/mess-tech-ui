'use client';

import React, { useState } from 'react';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { useCartStore } from '@/stores/useCartStore';
import { useCompareStore } from '@/stores/useCompareStore';
import { mockProducts } from '@/services/mockData';
import { formatPrice } from '@/lib/utils';
import {
  ShoppingCart,
  Scale,
  ShieldCheck,
  Truck,
  CheckCircle2,
  Star,
  Plus,
  Minus,
  Check,
  FileText,
} from 'lucide-react';

export default function ProductDetailPage() {
  const params = useParams();
  const { locale, t } = useLanguage();
  const addItem = useCartStore((state) => state.addItem);
  const { addToCompare, isInCompare } = useCompareStore();

  const [quantity, setQuantity] = useState(1);
  const [activeTab, setActiveTab] = useState<'specs' | 'desc'>('specs');

  const productId = params?.id as string;
  const product = mockProducts.find((p) => p.id === productId) || mockProducts[0];
  const inCompare = isInCompare(product.id);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">
      {/* Breadcrumb */}
      <nav className="text-xs text-slate-500 flex items-center gap-1.5">
        <Link href="/" className="hover:text-petrol-700">{t('nav_home')}</Link>
        <span>/</span>
        <Link href={`/catalog?category=${product.category}`} className="hover:text-petrol-700">
          {product.category.toUpperCase()}
        </Link>
        <span>/</span>
        <span className="text-petrol-900 font-bold line-clamp-1">{product.name[locale]}</span>
      </nav>

      {/* Main PDP Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-subtle">
        {/* Gallery Image */}
        <div className="flex flex-col items-center justify-center p-6 bg-slate-50/60 rounded-2xl border border-slate-100">
          <div className="relative w-full max-w-md h-72 sm:h-96 flex items-center justify-center">
            {product.discountPercent && (
              <span className="absolute top-2 start-2 px-3 py-1 rounded-lg bg-rose-600 text-white text-xs font-black">
                خصم {product.discountPercent}%
              </span>
            )}
            <img
              src={product.image}
              alt={product.name[locale]}
              className="max-h-full max-w-full object-contain hover:scale-105 transition-transform duration-300"
            />
          </div>
        </div>

        {/* Product Info */}
        <div className="space-y-6 flex flex-col justify-between">
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <span className="px-3 py-1 rounded-md bg-petrol-50 text-petrol-800 font-mono font-bold text-xs border border-petrol-200">
                {product.brand}
              </span>
              <span className="text-xs text-slate-400 font-mono">
                Model: {product.model}
              </span>
            </div>

            <h1 className="text-xl sm:text-2xl font-black text-petrol-950 leading-tight">
              {product.name[locale]}
            </h1>

            {/* Rating & Stock */}
            <div className="flex items-center gap-4 text-xs pt-1">
              <div className="flex items-center gap-1 text-amber-500 font-bold">
                <Star className="w-4 h-4 fill-amber-400" />
                <span>{product.rating}</span>
                <span className="text-slate-400 font-normal">({product.reviewsCount} تقييم)</span>
              </div>
              <span className="text-slate-300">|</span>
              <span className="text-emerald-600 font-bold flex items-center gap-1">
                <Check className="w-4 h-4" />
                <span>{t('inStock')} ({product.stockCount} قطعة متبقية)</span>
              </span>
            </div>

            {/* Price Box */}
            <div className="p-4 rounded-2xl bg-petrol-50/50 border border-petrol-100 flex items-baseline gap-4">
              <span className="text-2xl sm:text-3xl font-black text-petrol-900 font-mono">
                {formatPrice(product.price, locale)}
              </span>
              {product.oldPrice && (
                <span className="text-sm text-slate-400 line-through font-mono">
                  {formatPrice(product.oldPrice, locale)}
                </span>
              )}
            </div>

            {/* Brief */}
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
              {product.brief[locale]}
            </p>
          </div>

          {/* Actions & Quantity */}
          <div className="space-y-4 pt-4 border-t border-slate-100">
            <div className="flex items-center gap-4">
              {/* Quantity */}
              <div className="flex items-center border-2 border-slate-200 rounded-xl bg-white p-1">
                <button
                  onClick={() => setQuantity(Math.max(1, quantity - 1))}
                  className="p-2 text-slate-600 hover:text-petrol-700"
                >
                  <Minus className="w-4 h-4" />
                </button>
                <span className="px-4 font-mono font-bold text-sm text-petrol-900">{quantity}</span>
                <button
                  onClick={() => setQuantity(quantity + 1)}
                  className="p-2 text-slate-600 hover:text-petrol-700"
                >
                  <Plus className="w-4 h-4" />
                </button>
              </div>

              {/* Add to Cart */}
              <button
                onClick={() => addItem(product, quantity)}
                className="flex-1 py-3 px-6 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-black text-sm flex items-center justify-center gap-2 shadow-md hover:shadow-lg transition-all"
              >
                <ShoppingCart className="w-5 h-5 text-sky-300" />
                <span>{t('addToCart')}</span>
              </button>

              {/* Compare */}
              <button
                onClick={() => addToCompare(product)}
                className={`p-3 rounded-xl border transition-all ${
                  inCompare
                    ? 'bg-sky-600 text-white border-sky-600'
                    : 'border-slate-200 text-slate-600 hover:bg-slate-50'
                }`}
                title={t('addToCompare')}
              >
                <Scale className="w-5 h-5" />
              </button>
            </div>

            {/* Trust highlights */}
            <div className="grid grid-cols-2 gap-3 pt-2 text-xs text-slate-600">
              <div className="flex items-center gap-2 p-2.5 rounded-xl bg-slate-50">
                <Truck className="w-4 h-4 text-sky-600 shrink-0" />
                <span>شحن وتوصيل 24-48 ساعة لجميع المحافظات</span>
              </div>
              <div className="flex items-center gap-2 p-2.5 rounded-xl bg-slate-50">
                <ShieldCheck className="w-4 h-4 text-emerald-600 shrink-0" />
                <span>ضمان الوكيل المعتمد في مصر 12 شهر</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Tabs: Specifications & Datasheet */}
      <div className="bg-white rounded-3xl border border-slate-200 shadow-subtle p-6 sm:p-8 space-y-6">
        <div className="flex items-center gap-4 border-b border-slate-200 pb-3">
          <button
            onClick={() => setActiveTab('specs')}
            className={`font-black text-sm pb-2 border-b-2 transition-all ${
              activeTab === 'specs'
                ? 'border-petrol-700 text-petrol-900'
                : 'border-transparent text-slate-400 hover:text-slate-700'
            }`}
          >
            المواصفات التقنية (Datasheet Specs)
          </button>
          <button
            onClick={() => setActiveTab('desc')}
            className={`font-black text-sm pb-2 border-b-2 transition-all ${
              activeTab === 'desc'
                ? 'border-petrol-700 text-petrol-900'
                : 'border-transparent text-slate-400 hover:text-slate-700'
            }`}
          >
            تفاصيل الاستخدام والربط
          </button>
        </div>

        {activeTab === 'specs' ? (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {product.specs.map((sp, idx) => (
              <div
                key={idx}
                className="flex items-center justify-between p-3.5 rounded-xl bg-slate-50/70 border border-slate-100 text-xs"
              >
                <span className="font-bold text-slate-600">{sp.key[locale]}</span>
                <span className="font-mono font-bold text-petrol-900">{sp.value[locale]}</span>
              </div>
            ))}
          </div>
        ) : (
          <div className="prose text-xs text-slate-600 space-y-3 leading-relaxed">
            <p>{product.brief[locale]}</p>
            <p>
              يتم توريد هذا الجهاز كاملاً مع الكابلات الأصلية ومحولات الطاقة ودليل التثبيت السريع مع دعم فني متخصص لمساعدة فريق IT في تجهيز الإعدادات المبدئية.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
