'use client';

import React from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { useCartStore } from '@/stores/useCartStore';
import { formatPrice } from '@/lib/utils';
import { X, Trash2, Plus, Minus, ShoppingBag, ArrowLeft, ArrowRight, ShieldCheck } from 'lucide-react';

export default function CartDrawer() {
  const { locale, dir, t } = useLanguage();
  const { items, isOpen, closeCart, updateQuantity, removeItem, getSubtotal } = useCartStore();

  const subtotal = getSubtotal();
  const freeShippingThreshold = 10000;
  const progressToFree = Math.min(100, Math.round((subtotal / freeShippingThreshold) * 100));

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 overflow-hidden">
      {/* Backdrop */}
      <div
        onClick={closeCart}
        className="absolute inset-0 bg-petrol-950/60 backdrop-blur-xs transition-opacity"
      />

      {/* Drawer */}
      <div className={`absolute inset-y-0 ${dir === 'rtl' ? 'left-0' : 'right-0'} max-w-md w-full bg-white shadow-2xl flex flex-col z-10 animate-in slide-in-from-start duration-200`}>
        {/* Header */}
        <div className="p-4 sm:p-5 border-b border-slate-200 flex items-center justify-between bg-petrol-800 text-white">
          <div className="flex items-center gap-2">
            <ShoppingBag className="w-5 h-5 text-sky-400" />
            <h3 className="font-extrabold text-base">{t('myCart')}</h3>
            <span className="text-xs bg-petrol-700 px-2 py-0.5 rounded-full text-petrol-200 font-mono">
              ({items.length})
            </span>
          </div>

          <button
            onClick={closeCart}
            className="p-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-petrol-700 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Free Shipping Bar */}
        <div className="p-3 bg-sky-50 border-b border-sky-100 text-xs">
          <div className="flex items-center justify-between text-petrol-900 font-bold mb-1.5">
            <span>{t('freeShippingThreshold')}</span>
            <span className="font-mono text-sky-700">{progressToFree}%</span>
          </div>
          <div className="w-full h-1.5 bg-sky-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-sky-600 rounded-full transition-all duration-300"
              style={{ width: `${progressToFree}%` }}
            />
          </div>
        </div>

        {/* Items List */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {items.length === 0 ? (
            <div className="h-full flex flex-col items-center justify-center text-center p-6 space-y-3">
              <div className="w-16 h-16 rounded-full bg-slate-100 flex items-center justify-center text-slate-400">
                <ShoppingBag className="w-8 h-8" />
              </div>
              <h4 className="font-bold text-base text-slate-700">{t('cartEmpty')}</h4>
              <p className="text-xs text-slate-500 max-w-xs">{t('cartEmptyDesc')}</p>
              <button
                onClick={closeCart}
                className="mt-3 px-5 py-2.5 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs"
              >
                {t('startShopping')}
              </button>
            </div>
          ) : (
            items.map((item) => (
              <div
                key={item.product.id}
                className="flex items-center gap-3.5 p-3 rounded-xl border border-slate-200 bg-slate-50/50 hover:bg-white transition-all"
              >
                {/* Image */}
                <div className="w-16 h-16 rounded-lg bg-white p-1 border border-slate-200 flex items-center justify-center shrink-0">
                  <img
                    src={item.product.image}
                    alt={item.product.name[locale]}
                    className="max-h-full max-w-full object-contain"
                  />
                </div>

                {/* Details */}
                <div className="flex-1 min-w-0">
                  <h4 className="font-bold text-xs text-petrol-900 line-clamp-1 leading-snug">
                    {item.product.name[locale]}
                  </h4>
                  <span className="text-[10px] font-mono text-slate-400 block mb-1">
                    {item.product.model}
                  </span>
                  <span className="text-xs font-black text-petrol-700 font-mono">
                    {formatPrice(item.product.price, locale)}
                  </span>
                </div>

                {/* Quantity Controls */}
                <div className="flex items-center gap-1.5">
                  <div className="flex items-center border border-slate-200 rounded-lg bg-white">
                    <button
                      onClick={() => updateQuantity(item.product.id, item.quantity - 1)}
                      className="p-1 text-slate-500 hover:text-petrol-700"
                    >
                      <Minus className="w-3 h-3" />
                    </button>
                    <span className="px-2 text-xs font-bold font-mono text-slate-800">
                      {item.quantity}
                    </span>
                    <button
                      onClick={() => updateQuantity(item.product.id, item.quantity + 1)}
                      className="p-1 text-slate-500 hover:text-petrol-700"
                    >
                      <Plus className="w-3 h-3" />
                    </button>
                  </div>

                  <button
                    onClick={() => removeItem(item.product.id)}
                    className="p-1.5 text-rose-500 hover:bg-rose-50 rounded-lg transition-colors"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            ))
          )}
        </div>

        {/* Footer Summary & Checkout Button */}
        {items.length > 0 && (
          <div className="p-4 sm:p-5 border-t border-slate-200 bg-slate-50 space-y-3">
            <div className="flex items-center justify-between text-sm">
              <span className="text-slate-600 font-medium">{t('subtotal')}</span>
              <span className="font-black text-petrol-900 text-base font-mono">
                {formatPrice(subtotal, locale)}
              </span>
            </div>

            <div className="flex items-center justify-between text-xs text-slate-500">
              <span>{t('shipping')}</span>
              <span className="text-emerald-600 font-bold">
                {subtotal >= freeShippingThreshold ? t('freeShipping') : t('calculatedAtCheckout')}
              </span>
            </div>

            <div className="pt-2">
              <Link
                href="/checkout"
                onClick={closeCart}
                className="w-full py-3.5 px-4 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-extrabold text-sm flex items-center justify-center gap-2 shadow-md hover:shadow-lg transition-all"
              >
                <span>{t('checkoutBtn')}</span>
                {dir === 'rtl' ? <ArrowLeft className="w-4 h-4" /> : <ArrowRight className="w-4 h-4" />}
              </Link>
            </div>

            <div className="flex items-center justify-center gap-2 text-[11px] text-slate-500 pt-1">
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
              <span>{t('trust_cod_title')}</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
