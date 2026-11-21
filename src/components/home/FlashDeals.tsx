'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { useCartStore } from '@/stores/useCartStore';
import { mockProducts } from '@/services/mockData';
import { formatPrice } from '@/lib/utils';
import { Clock, Zap, ShoppingCart } from 'lucide-react';

export default function FlashDeals() {
  const { locale, t } = useLanguage();
  const addItem = useCartStore((state) => state.addItem);

  // Countdown timer: 14 hours 22 minutes 45 seconds
  const [timeLeft, setTimeLeft] = useState({
    hours: 14,
    minutes: 22,
    seconds: 45,
  });

  useEffect(() => {
    const timer = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev.seconds > 0) {
          return { ...prev, seconds: prev.seconds - 1 };
        } else if (prev.minutes > 0) {
          return { ...prev, minutes: prev.minutes - 1, seconds: 59 };
        } else if (prev.hours > 0) {
          return { ...prev, hours: prev.hours - 1, minutes: 59, seconds: 59 };
        }
        return prev;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  // Pick first 2 items with highest discount
  const dealProducts = mockProducts.filter((p) => p.discountPercent && p.discountPercent > 10).slice(0, 2);

  return (
    <section className="py-8 bg-gradient-to-r from-petrol-900 via-petrol-800 to-petrol-900 text-white border-y border-petrol-700">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col lg:flex-row items-center justify-between gap-6 mb-8">
          {/* Header */}
          <div className="space-y-1 text-center lg:text-start">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-400 text-petrol-950 font-black text-xs uppercase tracking-wider">
              <Zap className="w-3.5 h-3.5 fill-petrol-950" />
              <span>LIMITED OFFER</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-black text-white">{t('flashDealsTitle')}</h2>
            <p className="text-xs text-petrol-200">{t('flashDealsSubtitle')}</p>
          </div>

          {/* Countdown timer */}
          <div className="flex items-center gap-3">
            <Clock className="w-5 h-5 text-amber-400" />
            <div className="flex items-center gap-2 font-mono font-bold text-sm">
              <div className="bg-petrol-950/80 px-3 py-1.5 rounded-lg border border-petrol-700 text-center min-w-[48px]">
                <span className="text-lg text-amber-300 block leading-tight">{String(timeLeft.hours).padStart(2, '0')}</span>
                <span className="text-[9px] text-slate-400 uppercase">Hours</span>
              </div>
              <span className="text-amber-400 font-bold">:</span>
              <div className="bg-petrol-950/80 px-3 py-1.5 rounded-lg border border-petrol-700 text-center min-w-[48px]">
                <span className="text-lg text-amber-300 block leading-tight">{String(timeLeft.minutes).padStart(2, '0')}</span>
                <span className="text-[9px] text-slate-400 uppercase">Mins</span>
              </div>
              <span className="text-amber-400 font-bold">:</span>
              <div className="bg-petrol-950/80 px-3 py-1.5 rounded-lg border border-petrol-700 text-center min-w-[48px]">
                <span className="text-lg text-amber-300 block leading-tight">{String(timeLeft.seconds).padStart(2, '0')}</span>
                <span className="text-[9px] text-slate-400 uppercase">Secs</span>
              </div>
            </div>
          </div>
        </div>

        {/* 2 Deal Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {dealProducts.map((p) => (
            <div
              key={p.id}
              className="bg-white rounded-2xl p-4 sm:p-5 flex flex-col sm:flex-row items-center gap-5 text-slate-900 border border-petrol-700/50 shadow-lg"
            >
              <div className="w-32 h-32 sm:w-40 sm:h-40 shrink-0 bg-slate-50 p-2 rounded-xl flex items-center justify-center">
                <img src={p.image} alt={p.name[locale]} className="max-h-full max-w-full object-contain" />
              </div>

              <div className="flex-1 space-y-2 text-center sm:text-start">
                <span className="text-[10px] font-mono font-bold uppercase px-2 py-0.5 rounded bg-rose-50 text-rose-700 border border-rose-200">
                  خصم {p.discountPercent}% OFF
                </span>

                <h3 className="font-bold text-sm sm:text-base text-petrol-950 line-clamp-2 leading-snug">
                  {p.name[locale]}
                </h3>

                <p className="text-xs text-slate-500 line-clamp-2">{p.brief[locale]}</p>

                <div className="flex items-baseline justify-center sm:justify-start gap-3 pt-1">
                  <span className="text-lg sm:text-xl font-black text-rose-600 font-mono">
                    {formatPrice(p.price, locale)}
                  </span>
                  {p.oldPrice && (
                    <span className="text-xs text-slate-400 line-through font-mono">
                      {formatPrice(p.oldPrice, locale)}
                    </span>
                  )}
                </div>

                <div className="pt-2">
                  <button
                    onClick={() => addItem(p, 1)}
                    className="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs flex items-center justify-center gap-2 transition-all shadow-xs"
                  >
                    <ShoppingCart className="w-4 h-4 text-sky-300" />
                    <span>{t('addToCart')}</span>
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
